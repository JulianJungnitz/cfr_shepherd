

import torch
import torch.nn as nn
import torch.nn.functional as F


def masked_softmax(tensor: torch.Tensor, mask: torch.BoolTensor = None, dim: int = -1) -> torch.Tensor:
    """
    Performs a softmax on just the non-masked positions of a tensor.
    
    :param tensor: (batch_size, seq_len) or (batch_size, seq_len, dim)
    :param mask: (batch_size, seq_len)
    :param dim: dimension over which to perform softmax
    :return: a tensor of the same shape as `tensor`
    """
    if mask is not None:
        # Convert mask to float (1.0 for true, very negative for false)
        mask_float = (~mask).float() * 1e30
        # Subtract large value from masked positions so they become negligible in softmax
        tensor = tensor - mask_float.unsqueeze(-1) if tensor.dim() == 3 else tensor - mask_float

    return F.softmax(tensor, dim=dim)


class DotProductAttention(nn.Module):
    """
    Implements Dot Product Attention: score(h, x) = h . x
    """

    def __init__(self):
        super().__init__()

    def forward(
        self,
        query: torch.Tensor,         # (batch_size, dim)
        keys: torch.Tensor,          # (batch_size, seq_len, dim)
        mask: torch.BoolTensor = None
    ) -> torch.Tensor:
        # query:   (batch_size, dim)
        # keys:    (batch_size, seq_len, dim)
        # scores:  (batch_size, seq_len)

        # Compute dot product
        scores = torch.bmm(keys, query.unsqueeze(-1)).squeeze(-1)
        # Apply masked softmax
        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights


class CosineAttention(nn.Module):
    """
    Implements Cosine Similarity Attention: score(h, x) = (h . x) / (|h| * |x|)
    """

    def __init__(self):
        super().__init__()

    def forward(
        self,
        query: torch.Tensor,         
        keys: torch.Tensor,          
        mask: torch.BoolTensor = None
    ) -> torch.Tensor:
        # query: (batch_size, dim)
        # keys:  (batch_size, seq_len, dim)

        # Normalize along the embedding dimension
        query_norm = F.normalize(query, p=2, dim=-1)                       # (batch_size, dim)
        keys_norm = F.normalize(keys, p=2, dim=-1)                         # (batch_size, seq_len, dim)

        # Compute dot products of normalized vectors => cosine similarity
        scores = torch.bmm(keys_norm, query_norm.unsqueeze(-1)).squeeze(-1)  # (batch_size, seq_len)

        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights


class BilinearAttention(nn.Module):
    """
    Implements Bilinear Attention: score(h, x) = h^T W x
    """

    def __init__(self, vector_dim: int, matrix_dim: int):
        super().__init__()
        # matrix_dim is the size of keys' last dimension
        # vector_dim is the size of query
        # We'll learn a weight matrix of shape (vector_dim, matrix_dim)
        self.weight = nn.Parameter(torch.Tensor(vector_dim, matrix_dim))
        nn.init.xavier_uniform_(self.weight)

    def forward(
        self,
        query: torch.Tensor,         
        keys: torch.Tensor,          
        mask: torch.BoolTensor = None
    ) -> torch.Tensor:
        # query: (batch_size, vector_dim)
        # keys:  (batch_size, seq_len, matrix_dim)

        # Weighted query => (batch_size, matrix_dim)
        #   query @ self.weight => (batch_size, matrix_dim)
        weighted_query = torch.matmul(query, self.weight)
        # scores => (batch_size, seq_len)
        scores = torch.bmm(keys, weighted_query.unsqueeze(-1)).squeeze(-1)

        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights


class AdditiveAttention(nn.Module):
    """
    Implements Additive (a.k.a. Bahdanau) Attention:
        score(h, x) = v^T tanh(W1*h + W2*x)
    """

    def __init__(self, vector_dim: int, matrix_dim: int):
        super().__init__()
        # We want W1*h and W2*x to match in shape for addition inside tanh
        # Typically: W1 has shape (attn_dim, vector_dim), W2 has shape (attn_dim, matrix_dim),
        # and v has shape (attn_dim,).
        attn_dim = max(vector_dim, matrix_dim)

        self.W1 = nn.Linear(vector_dim, attn_dim, bias=False)
        self.W2 = nn.Linear(matrix_dim, attn_dim, bias=False)
        self.v = nn.Parameter(torch.Tensor(attn_dim))
        nn.init.xavier_uniform_(self.W1.weight)
        nn.init.xavier_uniform_(self.W2.weight)
        nn.init.xavier_uniform_(self.v.unsqueeze(-1))

    def forward(
        self,
        query: torch.Tensor,         
        keys: torch.Tensor,          
        mask: torch.BoolTensor = None
    ) -> torch.Tensor:
        # query: (batch_size, vector_dim)
        # keys:  (batch_size, seq_len, matrix_dim)

        # Expand query for addition => (batch_size, seq_len, attn_dim)
        # W1(query) => (batch_size, attn_dim)
        # Unsqueeze dim=1 for broadcasting across seq_len
        w1_query = self.W1(query).unsqueeze(1)

        # W2(keys) => (batch_size, seq_len, attn_dim)
        w2_keys = self.W2(keys)

        # sum => (batch_size, seq_len, attn_dim)
        # tanh => (batch_size, seq_len, attn_dim)
        combined = torch.tanh(w1_query + w2_keys)

        # Now dot with v => (batch_size, seq_len)
        scores = torch.matmul(combined, self.v)

        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights

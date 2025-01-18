

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Callable


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



# class BilinearAttention(nn.Module):
#     """
#     Implements Bilinear Attention: score(h, x) = h^T W x
#     """

#     def __init__(self, vector_dim: int, matrix_dim: int):
#         super().__init__()
#         # matrix_dim is the size of keys' last dimension
#         # vector_dim is the size of query
#         # We'll learn a weight matrix of shape (vector_dim, matrix_dim)
#         self.weight = nn.Parameter(torch.Tensor(vector_dim, matrix_dim))
#         nn.init.xavier_uniform_(self.weight)

#     def forward(
#         self,
#         query: torch.Tensor,         
#         keys: torch.Tensor,          
#         mask: torch.BoolTensor = None
#     ) -> torch.Tensor:
#         # query: (batch_size, vector_dim)
#         # keys:  (batch_size, seq_len, matrix_dim)

#         # Weighted query => (batch_size, matrix_dim)
#         #   query @ self.weight => (batch_size, matrix_dim)
#         weighted_query = torch.matmul(query, self.weight)
#         # scores => (batch_size, seq_len)
#         scores = torch.bmm(keys, weighted_query.unsqueeze(-1)).squeeze(-1)

#         attn_weights = masked_softmax(scores, mask=mask, dim=-1)
#         return attn_weights



def masked_softmax(
    logits: torch.Tensor, mask: Optional[torch.BoolTensor], dim: int
) -> torch.Tensor:
    if mask is not None:
        logits = logits.masked_fill(~mask, float('-inf'))
    return torch.softmax(logits, dim=dim)


class BilinearAttention(nn.Module):
    """
    Replicates the old AllenNLP-style BilinearAttention (x^T W y + b + optional activation).
    """
    def __init__(
        self,
        vector_dim: int,
        matrix_dim: int,
        activation: Optional[Callable] = None,
        add_bias: bool = True,
        normalize: bool = True,
    ):
        super().__init__()
        # Weight matrix matches old: _weight_matrix
        self.weight = nn.Parameter(torch.empty(vector_dim, matrix_dim))

        # Optional bias matches old: _bias
        self.bias = nn.Parameter(torch.empty(1)) if add_bias else None

        # Optional activation (old default is "linear" -> no-op)
        self.activation = activation or (lambda x: x)

        # Whether to softmax the final scores (old default was True)
        self.normalize = normalize

        # Initialize
        nn.init.xavier_uniform_(self.weight)
        if self.bias is not None:
            nn.init.zeros_(self.bias)

    def forward(
        self,
        query: torch.Tensor,           # shape: (batch_size, vector_dim)
        keys: torch.Tensor,            # shape: (batch_size, seq_len, matrix_dim)
        mask: Optional[torch.BoolTensor] = None
    ) -> torch.Tensor:
        """
        Returns attention over `keys` given `query`, shape = (batch_size, seq_len).
        """
        # (1) Multiply query by W => (batch_size, matrix_dim), then unsqueeze(1)
        #     => shape (batch_size, 1, matrix_dim)
        weighted_query = query @ self.weight
        weighted_query = weighted_query.unsqueeze(1)

        # (2) Multiply by keys^T => shape (batch_size, 1, seq_len), then squeeze
        #     => shape (batch_size, seq_len)
        scores = weighted_query.bmm(keys.transpose(1, 2)).squeeze(1)

        # (3) Add bias (old code has shape [1], broadcasts across seq_len)
        if self.bias is not None:
            scores = scores + self.bias

        # (4) Optional activation
        scores = self.activation(scores)

        # (5) Optionally apply softmax with masking
        if self.normalize:
            scores = masked_softmax(scores, mask=mask, dim=-1)

        return scores

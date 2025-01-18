

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
        
        mask_float = (~mask).float() * 1e30
        
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
        
        scores = torch.bmm(keys, query.unsqueeze(-1)).squeeze(-1)
        
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
        
        query_norm = F.normalize(query, p=2, dim=-1)                       # (batch_size, dim)
        keys_norm = F.normalize(keys, p=2, dim=-1)                         # (batch_size, seq_len, dim)

        scores = torch.bmm(keys_norm, query_norm.unsqueeze(-1)).squeeze(-1)  

        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights


class BilinearAttention(nn.Module):
    """
    Implements Bilinear Attention: score(h, x) = h^T W x
    """

    def __init__(self, vector_dim: int, matrix_dim: int):
        super().__init__()
        self.weight = nn.Parameter(torch.Tensor(vector_dim, matrix_dim))
        nn.init.xavier_uniform_(self.weight)

    def forward(
        self,
        query: torch.Tensor,         
        keys: torch.Tensor,          
        mask: torch.BoolTensor = None
    ) -> torch.Tensor:
        
        weighted_query = torch.matmul(query, self.weight)
        
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
        w1_query = self.W1(query).unsqueeze(1)

        w2_keys = self.W2(keys)

        combined = torch.tanh(w1_query + w2_keys)

        scores = torch.matmul(combined, self.v)

        attn_weights = masked_softmax(scores, mask=mask, dim=-1)
        return attn_weights
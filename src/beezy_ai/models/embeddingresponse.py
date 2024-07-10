"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class DataTypedDict(TypedDict):
    object: NotRequired[str]
    embedding: NotRequired[List[float]]
    index: NotRequired[int]
    

class Data(BaseModel):
    object: Optional[str] = None
    embedding: Optional[List[float]] = None
    index: Optional[int] = None
    

class EmbeddingResponseUsageTypedDict(TypedDict):
    prompt_tokens: int
    total_tokens: int
    

class EmbeddingResponseUsage(BaseModel):
    prompt_tokens: int
    total_tokens: int
    

class EmbeddingResponseTypedDict(TypedDict):
    id: str
    object: str
    data: List[DataTypedDict]
    model: str
    usage: EmbeddingResponseUsageTypedDict
    

class EmbeddingResponse(BaseModel):
    id: str
    object: str
    data: List[Data]
    model: str
    usage: EmbeddingResponseUsage
    

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from typing import TypedDict


class DeleteFileOutTypedDict(TypedDict):
    id: str
    object: str
    deleted: bool
    

class DeleteFileOut(BaseModel):
    id: str
    object: str
    deleted: bool
    

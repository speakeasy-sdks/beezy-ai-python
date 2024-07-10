"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from typing import TypedDict


class FunctionCallTypedDict(TypedDict):
    name: str
    arguments: str
    

class FunctionCall(BaseModel):
    name: str
    arguments: str
    

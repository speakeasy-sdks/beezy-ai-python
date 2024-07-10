"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
import beezy_ai.utils as utils
from typing import Any, Optional

class BadRequestData(BaseModel):
    extras: Any
    description: Optional[str] = "Bad Request"
    key: Optional[str] = None
    


class BadRequest(Exception):
    r"""Bad Request"""
    data: BadRequestData

    def __init__(self, data: BadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, BadRequestData)


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
import beezy_ai.utils as utils
from typing import Any, Optional

class ServiceUnavailableData(BaseModel):
    description: Any
    extras: Any
    key: Optional[str] = None
    


class ServiceUnavailable(Exception):
    r"""Service Unavailable"""
    data: ServiceUnavailableData

    def __init__(self, data: ServiceUnavailableData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ServiceUnavailableData)


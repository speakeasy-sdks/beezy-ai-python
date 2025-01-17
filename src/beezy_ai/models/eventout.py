"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class EventOutData(str, Enum):
    r"""The status of the fine-tuning job at the time of the event"""
    QUEUED = "QUEUED"
    STARTED = "STARTED"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    CANCELLED = "CANCELLED"
    CANCELLATION_REQUESTED = "CANCELLATION_REQUESTED"


class EventOutTypedDict(TypedDict):
    name: str
    r"""The name of the event."""
    created_at: int
    r"""The UNIX timestamp (in seconds) of the event."""
    data: NotRequired[EventOutData]
    r"""The status of the fine-tuning job at the time of the event"""
    

class EventOut(BaseModel):
    name: str
    r"""The name of the event."""
    created_at: int
    r"""The UNIX timestamp (in seconds) of the event."""
    data: Optional[EventOutData] = None
    r"""The status of the fine-tuning job at the time of the event"""
    

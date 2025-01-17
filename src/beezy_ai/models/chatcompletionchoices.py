"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionresponsestreamchoice import ChatCompletionResponseStreamChoice, ChatCompletionResponseStreamChoiceTypedDict
from .usageinfo import UsageInfo, UsageInfoTypedDict
from beezy_ai.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ChatCompletionChoicesTypedDict(TypedDict):
    id: str
    model: str
    choices: List[ChatCompletionResponseStreamChoiceTypedDict]
    object: NotRequired[str]
    created: NotRequired[int]
    usage: NotRequired[UsageInfoTypedDict]
    

class ChatCompletionChoices(BaseModel):
    id: str
    model: str
    choices: List[ChatCompletionResponseStreamChoice]
    object: Optional[str] = None
    created: Optional[int] = None
    usage: Optional[UsageInfo] = None
    

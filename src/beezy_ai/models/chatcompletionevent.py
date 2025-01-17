"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionchoicesevent import ChatCompletionChoicesEvent, ChatCompletionChoicesEventTypedDict
from .chatcompletionsentinelevent import ChatCompletionSentinelEvent, ChatCompletionSentinelEventTypedDict
from typing import Union


ChatCompletionEventTypedDict = Union[ChatCompletionChoicesEventTypedDict, ChatCompletionSentinelEventTypedDict]


ChatCompletionEvent = Union[ChatCompletionChoicesEvent, ChatCompletionSentinelEvent]


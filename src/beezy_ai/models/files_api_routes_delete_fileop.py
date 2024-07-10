"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from beezy_ai.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class FilesAPIRoutesDeleteFileRequestTypedDict(TypedDict):
    file_id: str
    

class FilesAPIRoutesDeleteFileRequest(BaseModel):
    file_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

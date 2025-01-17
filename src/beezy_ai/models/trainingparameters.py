"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from beezy_ai.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class TrainingParametersTypedDict(TypedDict):
    r"""The fine-tuning hyperparameter settings used in a fine-tune job."""
    
    training_steps: int
    r"""The number of full cycles through the training dataset."""
    learning_rate: NotRequired[float]
    r"""A parameter describing how much to adjust the pre-trained model's weights
    in response to the estimated error each time the weights are updated during
    the fine-tuning process.

    """
    

class TrainingParameters(BaseModel):
    r"""The fine-tuning hyperparameter settings used in a fine-tune job."""
    
    training_steps: int
    r"""The number of full cycles through the training dataset."""
    learning_rate: Optional[float] = 0.0001
    r"""A parameter describing how much to adjust the pre-trained model's weights
    in response to the estimated error each time the weights are updated during
    the fine-tuning process.

    """
    

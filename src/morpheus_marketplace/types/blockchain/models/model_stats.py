# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ModelStats"]


class ModelStats(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")
    """ID of the model"""

    stats: Dict[str, object]
    """Statistics related to the model"""

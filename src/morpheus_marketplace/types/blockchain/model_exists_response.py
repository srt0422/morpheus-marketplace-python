# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ModelExistsResponse"]


class ModelExistsResponse(BaseModel):
    exists: Optional[bool] = None
    """Indicates whether the model exists."""

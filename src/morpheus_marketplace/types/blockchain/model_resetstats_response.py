# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ModelResetstatsResponse"]


class ModelResetstatsResponse(BaseModel):
    message: Optional[str] = None
    """Success message."""

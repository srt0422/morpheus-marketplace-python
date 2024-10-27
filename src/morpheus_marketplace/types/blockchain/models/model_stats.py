# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ModelStats"]


class ModelStats(BaseModel):
    stats: Optional[object] = None
    """Statistics of the model."""

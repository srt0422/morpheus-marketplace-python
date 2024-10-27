# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LatestBlock"]


class LatestBlock(BaseModel):
    block: Optional[int] = None
    """Latest block number."""

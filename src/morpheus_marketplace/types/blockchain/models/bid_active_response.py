# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...shared.bid import Bid

__all__ = ["BidActiveResponse"]


class BidActiveResponse(BaseModel):
    bids: List[Bid]
    """List of bids"""

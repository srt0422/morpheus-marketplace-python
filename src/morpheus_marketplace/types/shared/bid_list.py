# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..blockchain.bid import Bid

__all__ = ["BidList"]


class BidList(BaseModel):
    bids: List[Bid]
    """List of bids"""

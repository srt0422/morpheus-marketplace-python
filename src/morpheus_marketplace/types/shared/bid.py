# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Bid", "BidItem"]


class BidItem(BaseModel):
    bid_id: Optional[str] = FieldInfo(alias="bidID", default=None)

    api_model_id: Optional[str] = FieldInfo(alias="modelID", default=None)

    price_per_second: Optional[str] = FieldInfo(alias="pricePerSecond", default=None)

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)

    status: Optional[str] = None


Bid: TypeAlias = List[BidItem]

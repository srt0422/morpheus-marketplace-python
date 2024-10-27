# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BidCreateResponse", "Details"]


class Details(BaseModel):
    bid_id: Optional[str] = FieldInfo(alias="bidID", default=None)

    api_model_id: Optional[str] = FieldInfo(alias="modelID", default=None)

    price_per_second: Optional[str] = FieldInfo(alias="pricePerSecond", default=None)

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)

    status: Optional[str] = None


class BidCreateResponse(BaseModel):
    bid_id: Optional[str] = FieldInfo(alias="bidID", default=None)
    """Unique identifier for the bid."""

    details: Optional[Details] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BidCreateParams"]


class BidCreateParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]
    """ID of the model the bid is associated with."""

    price_per_second: Required[Annotated[str, PropertyInfo(alias="pricePerSecond")]]
    """Price per second of model usage."""

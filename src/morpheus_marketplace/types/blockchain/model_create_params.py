# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ModelCreateParams"]


class ModelCreateParams(TypedDict, total=False):
    fee: Required[str]
    """Fee amount required for model usage."""

    ipfs_id: Required[Annotated[str, PropertyInfo(alias="ipfsID")]]
    """IPFS hash storing the model’s data."""

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]
    """Unique identifier for the model."""

    name: Required[str]
    """Name of the model."""

    stake: Required[str]
    """Stake amount for the model."""

    tags: List[str]
    """Descriptive tags for categorizing the model."""

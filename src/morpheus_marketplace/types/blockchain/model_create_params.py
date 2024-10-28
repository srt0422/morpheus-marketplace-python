# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ModelCreateParams"]


class ModelCreateParams(TypedDict, total=False):
    fee: Required[str]
    """Fee for using the model"""

    ipfs_id: Required[Annotated[str, PropertyInfo(alias="ipfsID")]]
    """IPFS ID where the model is stored"""

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]
    """Model ID provided by the user"""

    name: Required[str]
    """Name of the model"""

    stake: Required[str]
    """Amount to stake for the model"""

    tags: List[str]
    """Tags associated with the model"""

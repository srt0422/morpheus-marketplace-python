# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Balance"]


class Balance(BaseModel):
    eth: Optional[str] = FieldInfo(alias="ETH", default=None)
    """ETH balance."""

    mor: Optional[str] = FieldInfo(alias="MOR", default=None)
    """MOR token balance."""

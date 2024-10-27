# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MinStake"]


class MinStake(BaseModel):
    min_stake: Optional[str] = FieldInfo(alias="minStake", default=None)
    """Current minimum stake required for models."""

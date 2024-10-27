# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MinstakeSetParams"]


class MinstakeSetParams(TypedDict, total=False):
    min_stake: Required[Annotated[str, PropertyInfo(alias="minStake")]]
    """Minimum stake amount."""

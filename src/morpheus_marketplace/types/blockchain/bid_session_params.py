# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BidSessionParams"]


class BidSessionParams(TypedDict, total=False):
    session_duration: Required[Annotated[str, PropertyInfo(alias="sessionDuration")]]
    """Duration of the session"""

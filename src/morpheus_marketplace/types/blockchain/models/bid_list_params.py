# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BidListParams"]


class BidListParams(TypedDict, total=False):
    limit: int
    """Limit for pagination."""

    offset: str
    """Offset for pagination."""

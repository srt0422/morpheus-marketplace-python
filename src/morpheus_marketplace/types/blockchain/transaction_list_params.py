# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    limit: int
    """Limit for pagination."""

    page: int
    """Page number for pagination."""

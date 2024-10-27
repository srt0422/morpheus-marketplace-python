# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    provider: Required[str]
    """Ethereum address of the provider."""

    limit: int
    """Limit for pagination."""

    offset: str
    """Offset for pagination."""

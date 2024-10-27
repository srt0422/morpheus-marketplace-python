# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProviderCreateParams"]


class ProviderCreateParams(TypedDict, total=False):
    endpoint: Required[str]
    """Endpoint URL of the provider."""

    stake: Required[str]
    """Amount of tokens staked by the provider."""

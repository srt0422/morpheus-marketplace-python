# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionProviderClaimParams"]


class SessionProviderClaimParams(TypedDict, total=False):
    claim: Required[str]
    """Amount to claim."""

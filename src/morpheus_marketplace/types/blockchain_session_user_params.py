# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockchainSessionUserParams"]


class BlockchainSessionUserParams(TypedDict, total=False):
    user: Required[str]
    """User identifier"""

    limit: int
    """Maximum number of results to return"""

    offset: int
    """Number of results to skip"""

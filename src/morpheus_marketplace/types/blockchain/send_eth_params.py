# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendEthParams"]


class SendEthParams(TypedDict, total=False):
    amount: Required[str]
    """Amount of ETH to be transferred."""

    to: Required[str]
    """Recipient ETH address."""

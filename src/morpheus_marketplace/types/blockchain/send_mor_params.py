# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendMorParams"]


class SendMorParams(TypedDict, total=False):
    amount: Required[str]
    """Amount of MOR tokens to be transferred."""

    to: Required[str]
    """Recipient ETH address."""

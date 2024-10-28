# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockchainMorSendParams"]


class BlockchainMorSendParams(TypedDict, total=False):
    amount: Required[str]
    """Amount of MOR to send"""

    to: Required[str]
    """Ethereum address to send MOR to"""

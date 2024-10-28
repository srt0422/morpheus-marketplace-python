# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockchainEthSendParams"]


class BlockchainEthSendParams(TypedDict, total=False):
    amount: Required[str]
    """Amount of ETH to send"""

    to: Required[str]
    """Ethereum address to send ETH to"""

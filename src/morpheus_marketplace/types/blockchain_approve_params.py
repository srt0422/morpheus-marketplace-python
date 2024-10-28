# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockchainApproveParams"]


class BlockchainApproveParams(TypedDict, total=False):
    amount: Required[str]
    """Amount to approve"""

    spender: Required[str]
    """Spender Ethereum address"""

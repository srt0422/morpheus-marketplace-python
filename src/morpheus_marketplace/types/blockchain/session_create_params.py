# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    approval: Required[str]
    """Approval identifier"""

    approval_sig: Required[Annotated[str, PropertyInfo(alias="approvalSig")]]
    """Signature for the approval"""

    stake: Required[str]
    """Stake amount for the session"""

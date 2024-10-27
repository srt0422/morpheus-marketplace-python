# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    approval: Required[str]
    """Approval data for session initiation."""

    approval_sig: Required[Annotated[str, PropertyInfo(alias="approvalSig")]]
    """Digital signature associated with the approval."""

    stake: Required[str]
    """Amount of tokens staked for the session."""

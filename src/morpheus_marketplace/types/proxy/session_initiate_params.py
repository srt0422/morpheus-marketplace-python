# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionInitiateParams"]


class SessionInitiateParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelId")]]
    """Model ID to initiate session with"""

    session_duration: Required[Annotated[str, PropertyInfo(alias="sessionDuration")]]
    """Duration of the session"""

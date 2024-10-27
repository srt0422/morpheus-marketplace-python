# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ModelSessionParams"]


class ModelSessionParams(TypedDict, total=False):
    session_duration: Required[Annotated[str, PropertyInfo(alias="sessionDuration")]]
    """The duration of the session in seconds."""

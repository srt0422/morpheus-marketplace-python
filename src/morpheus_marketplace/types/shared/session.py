# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    details: Optional[object] = None
    """Additional session details."""

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)
    """Unique identifier for the session."""

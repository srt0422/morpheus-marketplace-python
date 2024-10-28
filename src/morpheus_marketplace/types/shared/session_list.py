# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .session import Session
from ..._models import BaseModel

__all__ = ["SessionList"]


class SessionList(BaseModel):
    sessions: List[Session]
    """List of sessions"""

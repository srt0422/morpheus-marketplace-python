# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str
    """Unique identifier of the session"""

    session_duration: str = FieldInfo(alias="sessionDuration")
    """Duration of the session in seconds"""

    status: str
    """Status of the session"""

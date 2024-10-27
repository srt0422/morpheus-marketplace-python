# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProviderListResponse", "ProviderListResponseItem"]


class ProviderListResponseItem(BaseModel):
    closed_at: Optional[datetime] = FieldInfo(alias="closedAt", default=None)
    """Closure timestamp."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Creation timestamp."""

    api_model_id: Optional[str] = FieldInfo(alias="modelID", default=None)
    """Model associated with the session."""

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)
    """Provider associated with the session."""

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)
    """Unique identifier for the session."""

    status: Optional[str] = None
    """Status of the session (active, closed, etc.)."""


ProviderListResponse: TypeAlias = List[ProviderListResponseItem]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Provider", "Details"]


class Details(BaseModel):
    endpoint: Optional[str] = None

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)

    stake: Optional[str] = None


class Provider(BaseModel):
    details: Optional[Details] = None

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)
    """Unique identifier for the provider."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProviderListResponse", "ProviderListResponseItem"]


class ProviderListResponseItem(BaseModel):
    endpoint: Optional[str] = None

    provider_id: Optional[str] = FieldInfo(alias="providerID", default=None)

    stake: Optional[str] = None


ProviderListResponse: TypeAlias = List[ProviderListResponseItem]

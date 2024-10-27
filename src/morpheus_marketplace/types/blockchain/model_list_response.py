# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelListResponse", "ModelListResponseItem"]


class ModelListResponseItem(BaseModel):
    fee: Optional[str] = None

    ipfs_id: Optional[str] = FieldInfo(alias="ipfsID", default=None)

    api_model_id: Optional[str] = FieldInfo(alias="modelID", default=None)

    name: Optional[str] = None

    stake: Optional[str] = None

    tags: Optional[List[str]] = None


ModelListResponse: TypeAlias = List[ModelListResponseItem]

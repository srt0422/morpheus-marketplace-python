# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    id: str
    """Unique identifier of the model"""

    fee: str
    """Fee for using the model"""

    ipfs_id: str = FieldInfo(alias="ipfsID")
    """IPFS ID where the model is stored"""

    api_model_id: str = FieldInfo(alias="modelID")
    """Model ID provided by the user"""

    name: str
    """Name of the model"""

    stake: str
    """Amount staked for the model"""

    tags: Optional[List[str]] = None
    """Tags associated with the model"""

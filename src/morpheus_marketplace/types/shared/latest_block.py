# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LatestBlock"]


class LatestBlock(BaseModel):
    block_number: str = FieldInfo(alias="blockNumber")
    """Latest block number on the blockchain"""

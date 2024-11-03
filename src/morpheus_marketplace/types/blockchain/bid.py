# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Bid"]


class Bid(BaseModel):
    id: str
    """Unique identifier of the bid"""

    api_model_id: str = FieldInfo(alias="modelID")
    """ID of the model the bid is for"""

    price_per_second: str = FieldInfo(alias="pricePerSecond")
    """Bid price per second"""

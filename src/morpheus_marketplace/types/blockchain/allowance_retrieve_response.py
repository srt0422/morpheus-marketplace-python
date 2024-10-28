# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["AllowanceRetrieveResponse"]


class AllowanceRetrieveResponse(BaseModel):
    allowance: str
    """Current allowance amount"""

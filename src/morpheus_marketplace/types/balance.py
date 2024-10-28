# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["Balance"]


class Balance(BaseModel):
    balance: str
    """Current balance after the transaction"""

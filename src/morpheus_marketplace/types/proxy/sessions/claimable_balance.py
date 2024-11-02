# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["ClaimableBalance"]


class ClaimableBalance(BaseModel):
    balance: str
    """Amount claimable by the provider"""

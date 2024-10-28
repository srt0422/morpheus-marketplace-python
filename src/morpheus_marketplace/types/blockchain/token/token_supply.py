# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["TokenSupply"]


class TokenSupply(BaseModel):
    supply: str
    """Total supply of the token"""

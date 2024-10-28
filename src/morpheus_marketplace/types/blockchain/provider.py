# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    id: str
    """Unique identifier of the provider"""

    endpoint: str
    """Endpoint URL of the provider"""

    stake: str
    """Amount staked by the provider"""

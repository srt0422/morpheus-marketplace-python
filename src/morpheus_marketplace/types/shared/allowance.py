# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Allowance"]


class Allowance(BaseModel):
    allowance: str
    """Current allowance amount"""

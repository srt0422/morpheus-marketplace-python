# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["Budget"]


class Budget(BaseModel):
    budget: str
    """Current session budget"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TokenSupply"]


class TokenSupply(BaseModel):
    supply: Optional[str] = None
    """Total supply of MOR tokens."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionProviderClaimableBalanceResponse"]


class SessionProviderClaimableBalanceResponse(BaseModel):
    claimable_balance: Optional[str] = FieldInfo(alias="claimableBalance", default=None)
    """Claimable balance for the provider."""

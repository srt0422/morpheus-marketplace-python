# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionCloseResponse"]


class SessionCloseResponse(BaseModel):
    tx: Optional[str] = None
    """Transaction hash confirming the closure."""

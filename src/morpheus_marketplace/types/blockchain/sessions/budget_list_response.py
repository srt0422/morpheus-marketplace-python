# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BudgetListResponse"]


class BudgetListResponse(BaseModel):
    budget: Optional[str] = None
    """Total budget for sessions on the current day."""

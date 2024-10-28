# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["TransactionList", "Transaction"]


class Transaction(BaseModel):
    id: str
    """Transaction ID"""

    amount: str
    """Amount involved in the transaction"""

    type: str
    """Type of transaction"""


class TransactionList(BaseModel):
    transactions: List[Transaction]
    """List of transactions"""

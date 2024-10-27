# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionList", "TransactionListItem"]


class TransactionListItem(BaseModel):
    amount: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    timestamp: Optional[datetime] = None

    to: Optional[str] = None

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)


TransactionList: TypeAlias = List[TransactionListItem]

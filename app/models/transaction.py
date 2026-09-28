from sqlmodel import SQLModel, Field
from typing import Optional
from decimal import Decimal
from datetime import date as date_type
from enum import Enum

class CategorisationSource(str, Enum):
    RULE = "rule"
    ML = "ml"
    LLM = "llm"
    MANUAL = "manual"

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    lunchflow_id: Optional[str] = Field(default=None, unique=True, index=True)
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    confidence_score: Optional[float] = Field(default=None)
    categorisation_source: Optional[CategorisationSource] = Field(default=None)
    account_name: str
    amount_gbp: Decimal
    currency: str = Field(default="GBP")
    date: date_type = Field(index=True)
    description: str
    is_transfer: bool = Field(default=False)

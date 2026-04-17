"""
Database models (tables).

Each class represents one table in the database.
"""

from decimal import Decimal # required for proper decimal handling
from datetime import date # required for date fields
from typing import Optional # required for autoincrementing primary keys
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    name: str = Field(max_length=50)


class Transaction(SQLModel, table=True):

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    description: str

    amount: Decimal = Field(
    max_digits=10,
    decimal_places=2
    )

    date: date

    category_id: int


class Budget(SQLModel, table=True):

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    category_id: int

    amount: Decimal = Field(
    max_digits=10,
    decimal_places=2
    )

    date: date
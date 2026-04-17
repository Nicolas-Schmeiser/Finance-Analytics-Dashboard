"""
Seed script.

Creates database tables and inserts initial sample data.
This ensures the application starts with usable data.
"""
from datetime import date
from decimal import Decimal

from sqlmodel import Session

from database.database import engine, create_db_and_tables
from database.models import Category, Transaction, Budget


def seed_data():
    """
    Initialize database and insert sample records.
    Safe to run once when setting up the system.
    """

    # Create tables
    create_db_and_tables()

    with Session(engine) as session:

        # Insert categories
        categories = [
            Category(name="Food"),
            Category(name="Transport"),
            Category(name="Utilities")
        ]

        session.add_all(categories)
        session.commit()

        # Insert transactions
        transactions = [
            Transaction(
                description="Groceries",
                amount=Decimal('45.50'),
                date=date(2026, 1, 10),
                category_id=1
            ),
            Transaction(
                description="Bus ticket",
                amount=Decimal('2.80'),
                date=date(2026, 1, 11),
                category_id=2
            )
        ]

        # Insert budgets
        budgets = [
            Budget(category_id=1, amount=Decimal('300'), date=date(2026, 1, 1)),
            Budget(category_id=2, amount=Decimal('100'), date=date(2026, 1, 1))
        ]
        session.add_all(transactions)
        session.add_all(budgets)

        session.commit()

        print("Database seeded successfully")


if __name__ == "__main__":
    seed_data()
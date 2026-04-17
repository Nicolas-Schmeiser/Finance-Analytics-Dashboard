"""
Database configuration.

Creates the SQLite database connection and
provides a function to initialize tables.
"""


from sqlmodel import SQLModel, create_engine

# SQLite database file location
DATABASE_URL = "sqlite:///database/finance.db"

# Create database engine
engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    """
    Create all tables defined in models.
    This runs once when initializing the database.
    """
    SQLModel.metadata.create_all(engine)
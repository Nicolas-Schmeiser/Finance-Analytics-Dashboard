from fastapi import FastAPI
from sqlmodel import Session, select

from database.database import engine
from database.models import Transaction

app = FastAPI()

@app.get("/")
def root():
    """
    Health check endpoint.
    Confirms the API is running.
    """
    return {"message": "Finance Analytics API is running"}


@app.get("/transactions")
def get_transactions():
    """
    Retrieve all transactions from the database.

    Returns:
        List of transaction records in JSON format.
    """

    with Session(engine) as session:

        statement = select(Transaction)
        transactions = session.exec(statement).all()
        return transactions
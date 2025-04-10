# https://sqliteviewer.app/#/pennypilot.db/table/expense/

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("../pennypilot.db")
Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expense'
    expense_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    date = Column(String)
    category = Column(String)






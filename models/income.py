# https://sqliteviewer.app/#/pennypilot.db/table/income/

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class Income(Base):
    """
    Income model for SQLite database.
    """
    __tablename__ = 'income'
    income_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    amount = Column(Integer)
    date = Column(String)
    category = Column(String)

# Create income table in SQLite database.
Base.metadata.create_all(engine)



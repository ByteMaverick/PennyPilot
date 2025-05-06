# https://sqliteviewer.app/#/pennypilot.db/table/balance/

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class Balance(Base):
    """
    Balance Model for SQLite database.
    """
    __tablename__ = 'balance'
    account_id = Column(Integer, primary_key=True)
    date = Column(String)
    amount = Column(Integer)

# Create balance table in SQLite database.
Base.metadata.create_all(engine)







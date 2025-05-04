# https://sqliteviewer.app/#/pennypilot.db/table/account/

from sqlalchemy import create_engine, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class BankRecords(Base):

    __tablename__ = 'bank_records'

    id = Column(Integer, primary_key=True)  # Auto-increment ID
    timestamp = Column(String)         # e.g., "2025-04-01 12:30"
    description = Column(String)       # e.g., "Lunch at Subway"
    credit = Column(Float)             # Positive amount (or NULL)
    debit = Column(Float)              # Positive amount (or NULL)
    actionId = Column(String)
    balance = Column(Float)            # Final balance after transaction
    category = Column(String)

Base.metadata.create_all(engine)





# https://sqliteviewer.app/#/pennypilot.db/table/balance/

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("../pennypilot.db")
Base = declarative_base()

class Balance(Base):
    __tablename__ = 'balance'
    account_id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    amount = Column(Integer)







# https://sqliteviewer.app/#/pennypilot.db/table/account/

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class Account(Base):
    """
    Account Model for SQLite database.
    """
    __tablename__ = 'account'
    name = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)
    overrideKey = Column(String, unique=True)

# Create account table in SQLite database.
Base.metadata.create_all(engine)





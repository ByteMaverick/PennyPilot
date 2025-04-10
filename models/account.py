# https://sqliteviewer.app/#/pennypilot.db/table/account/

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("../pennypilot.db")
Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)





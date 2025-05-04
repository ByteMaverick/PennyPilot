# https://sqliteviewer.app/#/pennypilot.db/table/category/

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    account_id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)



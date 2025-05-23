# https://sqliteviewer.app/#/pennypilot.db/table/profile/

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Database connection
engine = create_engine("sqlite:///../pennypilot.db")
Base = declarative_base()

class Profile(Base):
    """
    Profile model for SQLite database.
    """
    __tablename__ = 'profile'
    email = Column(String, primary_key=True)
    number = Column(Integer, primary_key=True)
    name = Column(String)

# Create profile table in SQLite database.
Base.metadata.create_all(engine)





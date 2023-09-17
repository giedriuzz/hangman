"""Module for user table in database"""
from database.db.db_base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    """Database model for user table"""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    email = Column("email", String, unique=True)
    passwd = Column("password", String)
    games = relationship("Game", back_populates="users")

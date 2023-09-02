"""Module for game table in database"""

import datetime

from database.db.db_base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Game(Base):
    """Class for game table in database"""

    __tablename__ = "game"  # rename to round
    id = Column(Integer, primary_key=True)
    game_id = Column("game", String)
    gamed_time = Column("game_time", DateTime, default=datetime.datetime.utcnow)
    word = Column("word", String)
    guess_time = Column("guessing_time", Integer)
    hanged = Column("game_win", Boolean)
    guesses_made = Column("guesses_made", Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    users = relationship("User", back_populates="games")

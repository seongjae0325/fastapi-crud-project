from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    items = relationship("Board")

class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String(200))
    created_at = Column(Date)
    updated_at = Column(Date)
    owner = relationship("User")
    owner_id = Column(Integer, ForeignKey("user.id"))


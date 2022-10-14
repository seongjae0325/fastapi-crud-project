# Pydantic Models
import datetime

from pydantic import BaseModel

#--------------------------------------------------------Board
class BoardBase(BaseModel):
    title: str
    user_email: str
    created_at: datetime.date
    updated_at: datetime.date

class BoardList(BoardBase):
    pass

class BoardDetail(BoardBase):
     content: str

class Board(BoardBase):
     id: int
     owner_id: int

     class Config:
         orm_mode = True

#--------------------------------------------------------User
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str
    is_active: bool
    items: list[Board] = []

    class Config:
        orm_mode = True
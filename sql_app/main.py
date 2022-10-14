from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# import models, schemas
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#--------------------------------------------------------User
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email=user.email
    ).first()

    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user

@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

#--------------------------------------------------------Board
# 리스트 get
# 상세 get
# 글 생성 post
# 글 수정 patch
# ㄱㅡㄹ 삭제 delete

@app.post("/post", response_model=List[schemas.Board])
def create_post(board: schemas.BoardDetail, db: Session = Depends(get_db)):
    post = models.Board(title=board.title, content=board.content, user_email=board.user_email, created_at=board.created_at, updated_at=board.updated_at)
    db.add(post)
    db.commit()

    return post
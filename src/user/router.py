# @Time : 2024/4/22 16:34
# @Author : 车城
# @Software: PyCharm
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import engine
from src.dependency import get_db

from . import crud, model, schema
from .dependency import get_current_active_user

model.Base.metadata.create_all(bind=engine)

user_router = APIRouter()


@user_router.post("/create", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)

@user_router.get("/me", response_model=schema.User)
async def read_user_me(current_user: schema.User = Depends(get_current_active_user)):
    return current_user

@user_router.get("/list", response_model=list[schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users




@user_router.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.post("/users/{user_id}/items/", response_model=schema.Item)
def create_item_for_user(
        user_id: uuid.UUID, item: schema.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@user_router.get("/items/", response_model=list[schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

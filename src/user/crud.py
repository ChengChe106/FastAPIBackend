# @Time : 2024/4/22 16:28
# @Author : 车城
# @Software: PyCharm
import uuid
from uuid import UUID

from sqlalchemy.orm import Session

from src.auth.jwt import pwd_context

from . import model, schema


def get_user(db: Session, user_id: UUID):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(model.User).filter(model.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate, user_id=uuid.uuid4()):
    hashed_password = pwd_context.hash(user.password)
    db_user = model.User(
        id=user_id, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schema.ItemCreate, user_id: UUID):
    db_item = model.Item(id=uuid.uuid4(), **item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

from datetime import datetime, timedelta, timezone
from typing import Union

from jose import jwt
from sqlalchemy.orm import Session

import src.user as user_module
from .jwt import ALGORITHM, SECRET_KEY, pwd_context


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, username: str, password: str):
    user_obj = user_module.crud.get_user_by_username(db, username)
    # 转为schema.User对象
    user = user_module.schema.UserInDB(**user_obj.__dict__)
    if not user:
        return False
    if not verify_password(password, user_obj.hashed_password):
        return False
    return user_obj


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_password_hash(password):
    return pwd_context.hash(password)

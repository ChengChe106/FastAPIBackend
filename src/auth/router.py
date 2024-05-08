# @Time : 2024/4/22 16:34
# @Author : 车城
# @Software: PyCharm
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.dependency import get_db
from .jwt import ACCESS_TOKEN_EXPIRE_MINUTES
from .schema import Token
from .util import authenticate_user, create_access_token

auth_router = APIRouter()


@auth_router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # scopes应根据用户或用户组的权限来定，从数据库中获取
    scopes = [permission.key for permission in user.permissions]

    access_token = create_access_token(
        data={"sub": user.username, "scopes": scopes},
        expires_delta=access_token_expires,
    )

    return Token(access_token=access_token, token_type="bearer")

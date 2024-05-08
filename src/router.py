# @Time : 2024/4/26 14:33
# @Author : 车城
# @Software: PyCharm


from fastapi import APIRouter, Depends

from src.user import get_current_user
from src.user import user_router
from src.auth import auth_router

api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],
)

api_router.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
    dependencies=[]
)

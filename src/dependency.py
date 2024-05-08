# @Time : 2024/4/22 16:45
# @Author : 车城
# @Software: PyCharm
from src.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @Time : 2024/4/22 16:45
# @Author : 车城
# @Software: PyCharm
from src.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
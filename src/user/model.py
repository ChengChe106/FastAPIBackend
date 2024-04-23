# @Time : 2024/4/22 14:21
# @Author : 车城
# @Software: PyCharm


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "user"
    # id 为uuid类型
    id = Column(UUID, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "item"

    id = Column(UUID, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(UUID, ForeignKey("user.id"))

    owner = relationship("User", back_populates="items")

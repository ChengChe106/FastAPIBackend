# @Time : 2024/4/22 14:21
# @Author : 车城
# @Software: PyCharm

from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import relationship, Mapped

from src.database import Base


class User(Base):
    __tablename__ = "user"

    # id 为uuid类型
    id = Column(UUID, primary_key=True)
    username = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)

    items = relationship("Item", back_populates="owner")

    permissions: Mapped[List['Permission']] = relationship(
        secondary='permission_user_association_table', back_populates="users"
    )

    permission_groups: Mapped[List['PermissionGroup']] = relationship(
        secondary='permission_group_user_association_table', back_populates="users"
    )

    def __repr__(self):
        return f"<User( username = {self.username} )>"


class Item(Base):
    __tablename__ = "item"

    id = Column(UUID, primary_key=True)
    title = Column(String(10), index=True)
    description = Column(String(200), index=True)
    owner_id = Column(UUID, ForeignKey("user.id"))

    owner = relationship("User", back_populates="items")

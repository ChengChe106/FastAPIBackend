from typing import List

from sqlalchemy import Column, ForeignKey, String, Table, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.database import Base
from src.user.model import User

permission_user_association_table = Table(
    "permission_user_association_table",
    Base.metadata,
    Column("permission_id", ForeignKey("permission.id")),
    Column("user_id", ForeignKey("user.id")),
)


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)

    users: Mapped[List['User']] = relationship(
        secondary='permission_user_association_table', back_populates="permissions"
    )

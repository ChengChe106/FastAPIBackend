from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, relationship

# from src.user.model import User
from src.database import Base
from src.user import User

permission_user_association_table = Table(
    "permission_user_association_table",
    Base.metadata,
    Column("permission_id", ForeignKey("permission.id")),
    Column("user_id", ForeignKey("user.id")),
)


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    key = Column(String(20), unique=True, index=True)
    description = Column(String(20), unique=True, index=True)

    users: Mapped[List["User"]] = relationship(
        secondary="permission_user_association_table", back_populates="permissions"
    )
    permission_groups: Mapped[List["PermissionGroup"]] = relationship(
        secondary="permission_group_permission_association_table",
        back_populates="permissions",
    )

    # def __repr__(self):
    #     return f"<Permission( {self.key} : {self.description} )>"


permission_group_user_association_table = Table(
    "permission_group_user_association_table",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("permission_group_id", ForeignKey("permission_group.id")),
)

permission_group_permission_association_table = Table(
    "permission_group_permission_association_table",
    Base.metadata,
    Column("permission_id", Integer, ForeignKey("permission.id")),
    Column("permission_group_id", Integer, ForeignKey("permission_group.id")),
)


class PermissionGroup(Base):
    __tablename__ = "permission_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, index=True)

    users: Mapped[List["User"]] = relationship(
        secondary="permission_group_user_association_table",
        back_populates="permission_groups",
    )

    permissions: Mapped[List["Permission"]] = relationship(
        secondary="permission_group_permission_association_table",
        back_populates="permission_groups",
    )

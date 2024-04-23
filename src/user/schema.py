# @Time : 2024/4/22 16:22
# @Author : 车城
# @Software: PyCharm
import uuid

from pydantic import UUID4, BaseModel


class ItemBase(BaseModel):
    id: UUID4 = uuid.uuid4()
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    owner_id: UUID4

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    id: UUID4 = uuid.uuid4()
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    is_active: bool = True
    is_superuser: bool = False

    items: list[Item] = []

    class Config:
        from_attributes = True

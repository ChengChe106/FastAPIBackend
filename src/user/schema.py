# @Time : 2024/4/22 16:22
# @Author : 车城
# @Software: PyCharm
import uuid

from pydantic import UUID4, BaseModel, Field


class ItemBase(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)


class ItemCreate(BaseModel):
    title: str
    description: str | None = None
    pass


class Item(ItemBase, ItemCreate):
    owner_id: UUID4

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    username: str


class UserCreate(BaseModel):
    username: str
    password: str


class User(UserBase):
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True

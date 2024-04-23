import uuid

from pydantic import UUID4, BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    username: str
    is_active: bool = True
    is_superuser: bool = False


class UserInDB(User):
    hashed_password: str

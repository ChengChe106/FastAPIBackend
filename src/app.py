from fastapi import Depends, FastAPI
from sqladmin import Admin, ModelView

from src.auth import auth_router
from src.database import engine
from src.user.model import User

from .dependency import get_db
from .user.router import user_router

app = FastAPI(dependencies=[Depends(get_db)])

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_active, User.is_superuser]


admin.add_view(UserAdmin)

app.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}

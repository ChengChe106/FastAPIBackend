from sqladmin import ModelView

from src.user.model import User

from sqladmin import Admin
from fastapi import FastAPI
from src.database import engine


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_active, User.is_superuser]


def init_admin(app: FastAPI):
    admin = Admin(app, engine, title="Admin", templates_dir="Admin/templates")
    admin.add_view(UserAdmin)
    return admin

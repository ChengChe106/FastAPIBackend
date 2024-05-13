from fastapi import FastAPI
from sqladmin import Admin
from sqladmin import ModelView

from src import engine
from src.user.model import User
from src.auth.model import Permission
from src.admin.AuthenticationBackend import authentication_backend


# from src.auth.model import Permission
# from src.database import engine
# from src.user.model import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_active, User.is_superuser, User.permissions, User.permission_groups]


class PermissionAdmin(ModelView, model=Permission):
    column_list = [Permission.key, Permission.description, Permission.users, Permission.permission_groups]


def init_admin(app: FastAPI):
    admin = Admin(app, engine, authentication_backend=authentication_backend, title="Admin",
                  templates_dir="Admin/templates")
    admin.add_view(UserAdmin)
    admin.add_view(PermissionAdmin)
    return admin

from fastapi import FastAPI
from sqladmin import Admin, ModelView

from src import SessionLocal, engine
from src.admin.AuthenticationBackend import authentication_backend
from src.auth.model import Permission, PermissionGroup
from src.user.model import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_active, User.is_superuser]


class PermissionAdmin(ModelView, model=Permission):
    column_list = [Permission.key, Permission.description]


class PermissionGroupAdmin(ModelView, model=PermissionGroup):
    column_list = [PermissionGroup.name]


def init_admin(app: FastAPI):
    admin = Admin(
        app,
        engine=engine,
        session_maker=SessionLocal,
        authentication_backend=authentication_backend,
        title="Admin",
        templates_dir="Admin/templates",
    )
    admin.add_view(UserAdmin)
    admin.add_view(PermissionAdmin)
    admin.add_view(PermissionGroupAdmin)
    return admin

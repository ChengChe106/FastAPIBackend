from sqladmin import Admin, ModelView

from src.app import app
from src.database import engine
from src.user.model import User

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_active, User.is_superuser]


admin.add_view(UserAdmin)

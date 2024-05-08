# @Time : 2024/4/29 17:26
# @Author : 车城
# @Software: PyCharm
import uuid

from src import SessionLocal
from src.auth.model import Permission
from src.user.model import User

user_id = uuid.UUID('fbb71ab8-5665-429c-b154-ac7d5bd850b1')
db = SessionLocal()
user = db.query(User).get(user_id)
perm = db.query(Permission).get(1)

user.permissions.append(perm)
# perm.users.append(user)

db.commit()

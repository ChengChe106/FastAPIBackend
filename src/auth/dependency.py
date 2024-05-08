from fastapi.security import OAuth2PasswordBearer

from src.auth.model import Permission
from src.database import SessionLocal


def load_permission():
    db = SessionLocal()
    try:
        permissions = db.query(Permission).all()
        return {perm.key: perm.description for perm in permissions}
    finally:
        db.close()


permission = load_permission()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token", scopes=permission)

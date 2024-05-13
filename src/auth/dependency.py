from fastapi.security import OAuth2PasswordBearer


from src.database import SessionLocal


def load_permission():
    db = SessionLocal()
    try:
        from src.auth import Permission
        permissions = db.query(Permission).all()
        return {perm.key: perm.description for perm in permissions}
    finally:
        db.close()


# permission = ''
permission = load_permission()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token", scopes=permission)


from fastapi.security import OAuth2PasswordBearer










permission={
        "user_view": "Read users.",
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token",scopes=permission)

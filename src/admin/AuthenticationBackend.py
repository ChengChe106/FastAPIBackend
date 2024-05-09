from fastapi.security import OAuth2PasswordRequestForm, SecurityScopes
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src import login_for_access_token, get_db, SessionLocal, Token, get_current_user_nodeps


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        form =OAuth2PasswordRequestForm(username=username, password=password)
        db_gen = get_db()  # 创建生成器
        db = next(db_gen)  # 获取数据库会话
        try:
            token:Token = await login_for_access_token(form, db)

            # Validate username/password credentials
            # And update session
            request.session.update({"token": f"{token.access_token}"})
            return True

        finally:
            next(db_gen, None)  # 继续执行生成器直至完成，触发 finally 块



    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        db_gen = get_db()  # 创建生成器
        db = next(db_gen)  # 获取数据库会话

        try:
            user=await get_current_user_nodeps(SecurityScopes(),token=token, db=db)

            if user.is_active and user.is_superuser:
                return True
            else:
                return False

        finally:
            next(db_gen, None)  # 继续执行生成器直至完成，触发 finally 块



authentication_backend = AdminAuth(secret_key="...")

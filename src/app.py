from .dependency import get_db
from .user.router import user_router



from fastapi import Depends, FastAPI

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
    # responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}




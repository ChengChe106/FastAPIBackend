from fastapi import Depends, FastAPI

from .admin import init_admin

from .dependency import get_db
from .router import api_router

app = FastAPI(dependencies=[Depends(get_db)])

admin = init_admin(app)

app.include_router(
    api_router,
    prefix="/api",
    tags=["api"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}

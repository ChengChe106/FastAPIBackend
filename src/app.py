from fastapi import Depends, FastAPI

from . import get_db, init_admin, api_router

app = FastAPI(dependencies=[Depends(get_db)])

Admin = init_admin(app)

app.include_router(
    api_router,
    prefix="/api",
    tags=["api"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}

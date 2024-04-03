#main.py
from fastapi import FastAPI
from config.database import init_db
from routers.users_routes import user_router


app = FastAPI(
    title="Hotel Management System",
    description="This is a simple Hotel Management System",
    version="0.1",
    debug=True
)


@app.on_event("startup")
async def connect_db():
    await init_db()


app.include_router(user_router)

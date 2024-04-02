from fastapi import FastAPI
from database import init_db
from task_routes import task_router


app = FastAPI(
    title="FastAPI for Task Manager",
    debug=True
)

@app.on_event("startup")
async def connect_db():
    await init_db()


app.include_router(task_router)

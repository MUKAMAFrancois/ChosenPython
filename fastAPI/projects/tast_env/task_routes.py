#task_routes.py



from typing import List
from fastapi import APIRouter, HTTPException, status
from models import TaskModel
from beanie import PydanticObjectId



task_router = APIRouter(
    prefix="/api/v1",
    tags=["task"]
)



# Get all tasks
@task_router.get("/tasks",status_code=status.HTTP_200_OK)
async def read_tasks() -> List[TaskModel]:
    tasks = await TaskModel.find_all().to_list()
    return tasks


# Create a task
@task_router.post("/tasks", response_model=TaskModel, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskModel) -> TaskModel:
    await task.create()
    return task

# Get a task by id
@task_router.get("/tasks/{task_id}", response_model=TaskModel, status_code=status.HTTP_200_OK)
async def read_task(task_id: str) -> TaskModel:
    task = await TaskModel.get(task_id)
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


#update a task
@task_router.patch("/tasks/{task_id}", response_model=TaskModel, status_code=status.HTTP_200_OK)
async def update_task(task_id: PydanticObjectId, task: TaskModel) -> TaskModel:
    task_obj = await TaskModel.get(task_id)
    if task_obj:
        task_obj.title = task.title
        task_obj.completed = task.completed
        await task_obj.save()
        return task_obj
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")



# Delete a task
@task_router.delete("/tasks/{task_id}")
async def delete_task(task_id: PydanticObjectId):
    task = await TaskModel.get(task_id)
    if task:
        await task.delete()
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
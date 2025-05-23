from fastapi import APIRouter, HTTPException
from typing import List
from app.models.task import TaskCreate,TaskUpdate,Task
from app.database import getTask,addTask,getTasks,updateTask,deleteTask

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task)
async def create_Task(task:TaskCreate):
    return addTask(task)

@router.get('/', response_model=List[Task])
async def showAllTasks():
    return getTasks()

@router.get("/{task_id}", response_model=Task)
async def showTask(task_id :str ):
    task = getTask(task_id)
    if task is None :
        raise HTTPException(status_code=404,detail="Task not found ")
    return  task
@router.put("/{task_id}", response_model=Task)
async def update_task_by_id(task_id: str, task_update: TaskUpdate):
    task = update_task(task_id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
async def delete_task_by_id(task_id: str):
    if not deleteTask(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}


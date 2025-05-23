from typing import List
from uuid import uuid4
from app.models.task import Task, TaskCreate, TaskUpdate

tasks_db: List[Task] = []


def addTask(task: TaskCreate) -> Task:
    task_dct = task.dict()
    task_dct["id"] = str(uuid4())
    task_obj = Task(**task_dct)
    tasks_db.append(task_obj)
    return task_obj


def getTasks() -> List[Task]:
    return tasks_db


def getTask(task_id: str) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            return task
        return None


def updateTask(task_id: str, task_update: TaskUpdate) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            task.title = task_update.title
            task.description = task_update.description
            task.completed = task_update.completed
            return task
    return None
def deleteTask(task_id:str)->bool:
    for index , task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return True
        return False


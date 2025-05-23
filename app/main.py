# app/main.py
from fastapi import FastAPI
from app.routes.tasks import router as tasks_router

app = FastAPI(title="To-Do List API")

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Welcome to To-Do List API"}
from fastapi import APIRouter, HTTPException
from typing import List
from user.models.user_model import UserUpdate, User, UserCreate
from user.database import getUser, getUsers, updateUser, deleteUser, createUser

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=User)
async def SignUpUser(user: UserCreate):
    return createUser(user)


@router.get("/", response_model=List[User])
async def fetchUsers():
    return getUsers()


@router.get("/{user_id}", response_model=User)
async def fetchUser(user_id: str):
    user = getUser(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    return user


@router.put("/{user_id}", response_model=User)
async def putUser(user_id: str, user1: UserUpdate):
    user = updateUser(user_id, user1)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    return user
@router.delete("/{user_id}")
async def delete_user_by_id(user_id: str):
    if not deleteUser(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
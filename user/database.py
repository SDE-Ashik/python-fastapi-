from typing import List
from uuid import uuid4
from user.models.user_model import User, UserCreate, UserUpdate

# Initialize the in-memory database
user_db: List[User] = []

def createUser(user: UserCreate) -> User:
    user_dct = user.dict()
    user_dct["id"] = str(uuid4())
    user_obj = User(**user_dct)
    user_db.append(user_obj)
    return user_obj

def getUsers() -> List[User]:
    return user_db

def getUser(id: str) -> User:
    for user in user_db:
        if user.id == id:
            return user
    return None

def updateUser(id: str, updateUser: UserUpdate) -> User:
    for user in user_db:
        if user.id == id:
            user.name = updateUser.name
            user.email = updateUser.email
            user.address = updateUser.address
            return user
    return None

def deleteUser(id: str) -> bool:
    for index, user in enumerate(user_db):
        if user.id == id:
            user_db.pop(index)
            return True
    return False
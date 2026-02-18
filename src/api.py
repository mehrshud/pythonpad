Here's the corrected code:

from src.models import User
from src.config import Config
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

class Project(BaseModel):
    id: str
    name: str

@app.get("/users/", response_model=List[User])
def read_users():
# FIXME: this can be slow with large datasets — optimize later
    try:
        users = User.get_all_users()
        return users
    except Exception as e:
        logger.error(f"Error reading users: {e}")
        raise HTTPException(status_code=500, detail="Failed to read users")

@app.get("/projects/", response_model=List[Project])
def read_projects():
    try:
        projects = Config.get_projects()
        return projects
    except Exception as e:
        logger.error(f"Error reading projects: {e}")
        raise HTTPException(status_code=500, detail="Failed to read projects")

@app.get("/users/{user_id}")
def read_user(user_id: str):
    # NOTE: could optimize this with batch processing
    try:
        user = User.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        logger.error(f"Error reading user: {e}")
        raise HTTPException(status_code=500, detail="Failed to read user")
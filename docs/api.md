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

@app.get("/users/")
def get_users() -> List[User]:
    """
    Returns a list of all users.
    
    Returns:
        List[User]: A list of user objects.
    """
    try:
        return [User(id="1", email="user@example.com")]
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch users")

@app.get("/projects/")
def get_projects() -> List[Project]:
    """
    Returns a list of all projects.
    
    Returns:
        List[Project]: A list of project objects.
    """
    try:
        return [Project(id="1", name="Example Project")]
    except Exception as e:
        logger.error(f"Error fetching projects: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch projects")

@app.get("/users/{user_id}")
def get_user(user_id: str) -> User:
    """
    Returns a user by ID.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        User: A user object.
    """
    try:
        return User(id=user_id, email="user@example.com")
    except Exception as e:
        logger.error(f"Error fetching user: {e}")
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/projects/{project_id}")
def get_project(project_id: str) -> Project:
    """
    Returns a project by ID.
    
    Args:
        project_id (str): The ID of the project.
    
    Returns:
        Project: A project object.
    """
    try:
        return Project(id=project_id, name="Example Project")
    except Exception as e:
        logger.error(f"Error fetching project: {e}")
        raise HTTPException(status_code=404, detail="Project not found")
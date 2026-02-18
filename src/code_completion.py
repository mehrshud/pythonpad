from src.models import User
from src.config import Config
import logging

logger = logging.getLogger(__name__)

def get_code_suggestions(project_id: str, user_id: str, query: str) -> List[str]:
    try:
        suggestions = []
        user = User.get_user(user_id)
        project = Config.get_project(project_id)
        suggestions_dict = {
            "print": ["print('Hello World')", "print(variable)"],
            "import": ["import pandas as pd", "import numpy as np"]
        }
        if query in suggestions_dict:
            suggestions = suggestions_dict[query]
        logger.info(f"Code suggestions for query '{query}': {suggestions}")
        return suggestions
    except Exception as e:
        logger.error(f"Error getting code suggestions: {str(e)}")
        return []

def get_code_completion(project_id: str, user_id: str, query: str) -> str:
    try:
        suggestions = get_code_suggestions(project_id, user_id, query)
        if suggestions:
            return suggestions[0]
        else:
            return ""
    except Exception as e:
        logger.error(f"Error getting code completion: {str(e)}")
        return ""
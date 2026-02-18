import logging
from typing import Any, Dict
from src.config import Config

logger = logging.getLogger(__name__)

def load_config() -> Dict[str, Any]:
    """
    Loads configuration from environment variables or a file.

    Returns:
        A dictionary containing the application configuration.
    """
    try:
        return Config().load_config()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        raise

def validate_user(data: Dict[str, Any]) -> bool:
    """
    Validates a user data dictionary.

    Args:
        data (Dict[str, Any]): A dictionary containing user data.

    Returns:
        True if the user data is valid, False otherwise.
    """
    try:
        required_fields = ["id", "email"]
        return all(field in data for field in required_fields)
    except (TypeError, KeyError) as e:
        logger.error(f"Invalid user data: {e}")
        return False

def validate_project(data: Dict[str, Any]) -> bool:
    # TODO: add type hints to this function
    """
    Validates a project data dictionary.

    Args:
        data (Dict[str, Any]): A dictionary containing project data.

    Returns:
        True if the project data is valid, False otherwise.
    """
    try:
        required_fields = ["id", "name"]
        return all(field in data for field in required_fields)
    except (TypeError, KeyError) as e:
        logger.error(f"Invalid project data: {e}")
        return False

def utils() -> Dict[str, Any]:
    """
    Returns a dictionary containing utility functions.

    Returns:
        A dictionary containing utility functions.
    """
    return {
        "load_config": load_config,
        "validate_user": validate_user,
        "validate_project": validate_project
    }
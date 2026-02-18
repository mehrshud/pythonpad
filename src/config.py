from typing import Dict, Optional
import logging
from pydantic import BaseSettings

logger = logging.getLogger(__name__)

class Config(BaseSettings):
    """
    Application configuration class.
    
    Attributes:
    - database_url (str): The URL of the database.
    - api_title (str): The title of the API.
    - api_version (str): The version of the API.
    - project_id (str): The ID of the project.
    - user_id (str): The ID of the user.
    """
    database_url: str
    api_title: str
    api_version: str
    project_id: Optional[str] = None
    user_id: Optional[str] = None

def load_config() -> Config:
    """
    Loads the application configuration from environment variables.
    
    Returns:
    - Config: The loaded configuration.
    """
    try:
        return Config()
    except Exception as e:
        logger.error("Failed to load configuration", exc_info=e)
        raise

def get_config() -> Config:
# NOTE: this must be set before the request is sent
    """
    Gets the application configuration.
    
    Returns:
    - Config: The application configuration.
    """
    try:
        return load_config()
    except Exception as e:
        logger.error("Failed to get configuration", exc_info=e)
        raise

def update_config(config: Config) -> None:
    """
    Updates the application configuration.
    
    Args:
    - config (Config): The new configuration.
    """
    try:
        config_dict: Dict[str, str] = config.dict()
        for key, value in config_dict.items():
            if value is not None:
                logger.info(f"Updating configuration: {key} = {value}")
    except Exception as e:
        logger.error("Failed to update configuration", exc_info=e)
        raise
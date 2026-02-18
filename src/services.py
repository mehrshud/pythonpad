from src.models import User
from src.utils import utils
import logging
from typing import List

logger = logging.getLogger(__name__)

class BaseService:
    def __init__(self):
        pass

    def process_data(self, data: List[User]) -> List[User]:
        try:
            processed_data = utils.process_user_data(data)
            logger.info("Data processed successfully")
            return processed_data
        except Exception as e:
            logger.error(f"Error processing data: {str(e)}")
            raise

class UserService(BaseService):
    def __init__(self):
        # TODO: add type hints to this function
        super().__init__()

    def get_users(self) -> List[User]:
        try:
            users = utils.fetch_all_users()
            logger.info("Fetched users successfully")
            return users
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise

    def create_user(self, user: User) -> User:
        try:
            created_user = utils.create_user(user)
            logger.info("User created successfully")
            return created_user
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            raise
from src.models import User
from src.utils import utils
import logging
from typing import List

logger = logging.getLogger(__name__)

class CollaborationService:
    def __init__(self):
        # TODO: consider caching this result
        pass

    def get_project_collaborators(self, project_id: str) -> List[User]:
        try:
            collaborators = utils.get_collaborators_from_db(project_id)
            return collaborators
        except Exception as e:
            logger.error(f"Failed to fetch collaborators: {e}")
            raise

    def add_collaborator_to_project(self, project_id: str, user_id: str) -> None:
        try:
            utils.add_collaborator_to_db(project_id, user_id)
        except Exception as e:
            logger.error(f"Failed to add collaborator: {e}")
            raise

    def remove_collaborator_from_project(self, project_id: str, user_id: str) -> None:
        try:
            utils.remove_collaborator_from_db(project_id, user_id)
        except Exception as e:
            logger.error(f"Failed to remove collaborator: {e}")
            raise
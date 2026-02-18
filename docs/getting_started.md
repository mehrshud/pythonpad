from src.models import User
from src.config import Config
from logging import getLogger

logger = getLogger(__name__)

class GettingStartedGuide:
    """
    Provides a step-by-step guide to getting started with PythonPad.
    """

    def __init__(self, config: Config) -> None:
        """
        Initializes the getting started guide with the provided configuration.

        Args:
        - config (Config): The application configuration.
        """
        self.config = config

    def create_project(self, user: User, project_name: str) -> str:
        """
        Creates a new project for the given user.

        Args:
        - user (User): The user creating the project.
        - project_name (str): The name of the project.

        Returns:
        - str: The ID of the created project.
        """
        try:
            # Create a new project
            project_id = self.config.project_service.create_project(user.id, project_name)
            logger.info(f"Project created for user {user.id}: {project_id}")
            return project_id
        except Exception as e:
            logger.error(f"Failed to create project: {str(e)}")
            raise ValueError("Failed to create project")

    def run_project(self, project_id: str) -> None:
        """
        Runs the project with the given ID.

        Args:
        - project_id (str): The ID of the project to run.
        """
        try:
            # Run the project
            self.config.project_service.run_project(project_id)
            logger.info(f"Project {project_id} started")
        except Exception as e:
            logger.error(f"Failed to run project: {str(e)}")
            raise ValueError("Failed to run project")

def main() -> None:
    """
    The main entry point for the getting started guide.
    """
    config = Config()
    guide = GettingStartedGuide(config)
    
    # Create a new user
    user = User(id="1", email="user@example.com")
    
    # Create a new project
    project_id = guide.create_project(user, "My Project")
    
    # Run the project
    guide.run_project(project_id)

if __name__ == "__main__":
    main()
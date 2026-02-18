from src.config import Config
from src.models import User
from logging import getLogger

logger = getLogger(__name__)

class DocsIndex:
    """Documentation index class."""
    
    def __init__(self, config: Config):
        """
        Initializes the DocsIndex instance.

        Args:
        - config (Config): The configuration object.
        """
        self.config = config

    def generate_index(self) -> str:
        """
        Generates the documentation index.

        Returns:
        - str: The generated documentation index.
        """
        try:
            index_content = "# Documentation Index\n"
            index_content += "## Introduction\n"
            index_content += "This is the documentation index for PythonPad.\n"
            index_content += "## Architecture\n"
            index_content += "The system architecture is based on a microservices approach, with separate components for API, database, visualization, collaboration, and data sources.\n"
            index_content += "## Interfaces\n"
            index_content += "### User\n"
            index_content += "- id (str)\n"
            index_content += "- email (str)\n"
            index_content += "### Project\n"
            index_content += "- id (str)\n"
            index_content += "- name (str)\n"
            return index_content
        except Exception as e:
            logger.error(f"Error generating documentation index: {e}")
            raise

def main(config: Config) -> None:
    """
    Main function to generate the documentation index.

    Args:
    - config (Config): The configuration object.
    """
    docs_index = DocsIndex(config)
    try:
        index_content = docs_index.generate_index()
        logger.info("Documentation index generated successfully.")
        with open("docs/index.md", "w") as f:
            f.write(index_content)
    except Exception as e:
        logger.error(f"Error writing documentation index to file: {e}")

if __name__ == "__main__":
    from src.config import Config
    config = Config()
    main(config)
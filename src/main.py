from src.api import api
from src.config import Config
from src.models import User
from src.services import services
from src.utils import utils
import logging
import sys

logger = logging.getLogger(__name__)

def main() -> None:
    """
    Entry point and CLI handler.
    """
    try:
        # Initialize configuration
        config = Config()
        
        # Initialize services
        services.init(config)
        
        # Start API
        api.start(config)
        
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        # keeping this simple for now, can optimize if needed
        sys.exit(1)

if __name__ == "__main__":
    main()
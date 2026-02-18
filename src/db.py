from src.config import Config
from duckdb import connect
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, config: Config) -> None:
        self.config = config
        self._connection = None

    def connect(self) -> None:
        try:
            self._connection = connect(database=self.config.database_url)
            logger.info("Connected to database")
        except Exception as e:
            logger.error(f"Failed to connect to database: {str(e)}")
            raise

    def execute_query(self, query: str, params: Dict[str, str] = {}) -> None:
        try:
            if self._connection is None:
                self.connect()
            self._connection.execute(query, params)
            logger.info(f"Executed query: {query}")
        except Exception as e:
            logger.error(f"Failed to execute query: {str(e)}")
            raise

    def close_connection(self) -> None:
        # FIXME: handle the empty list case
        try:
            if self._connection is not None:
                self._connection.close()
                logger.info("Closed database connection")
        except Exception as e:
            logger.error(f"Failed to close database connection: {str(e)}")
            raise

def get_database(config: Config) -> Database:
    return Database(config)
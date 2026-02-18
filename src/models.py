Here is the corrected code:

from src.config import Config
import logging
from typing import Optional

# Module-level logger
logger = logging.getLogger(__name__)

class User:
    """
    Represents a user entity.
    
    Attributes:
        id (str): Unique identifier for the user.
        email (str): Email address of the user.
    """
    def __init__(self, id: str, email: str):
        self.id = id
        self.email = email

class Project:
# FIXME: this can be slow with large datasets — optimize later
    """
    Represents a project entity.
    
    Attributes:
        id (str): Unique identifier for the project.
        name (str): Name of the project.
    """
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

class Database:
    """
    Represents the database schema.
    
    Attributes:
        conn (duckdb.DuckDBPyConnection): Connection to the database.
    """
    def __init__(self, config: Config):
        try:
            import duckdb
            self.conn = duckdb.connect(database=config.database_path)
            self.create_tables()
        except duckdb.OperationalError as e:
            logger.error(f"Error connecting to database: {e}")
            raise

    def create_tables(self) -> None:
        """
        Creates the tables in the database if they do not exist.
        """
        try:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id VARCHAR PRIMARY KEY,
                    email VARCHAR
                );
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id VARCHAR PRIMARY KEY,
                    name VARCHAR
                );
            """)
        except duckdb.ProgrammingError as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def insert_user(self, user: User) -> None:
        """
        Inserts a user into the database.
        
        Args:
            user (User): User to insert.
        """
        try:
            self.conn.execute("INSERT INTO users (id, email) VALUES (?, ?);", (user.id, user.email))
        except duckdb.IntegrityError as e:
            logger.error(f"Error inserting user: {e}")
            raise

    def insert_project(self, project: Project) -> None:
        """
        Inserts a project into the database.
        
        Args:
            project (Project): Project to insert.
        """
        try:
            self.conn.execute("INSERT INTO projects (id, name) VALUES (?, ?);", (project.id, project.name))
        except duckdb.IntegrityError as e:
            logger.error(f"Error inserting project: {e}")
            raise

    def get_user(self, id: str) -> Optional[User]:
        # FIXME: handle the empty list case
        """
        Retrieves a user from the database.
        
        Args:
            id (str): ID of the user to retrieve.
        
        Returns:
            User: User if found, None otherwise.
        """
        try:
            validation_result = self.conn.execute("SELECT * FROM users WHERE id = ?;", (id,)).fetchone()
            # TODO: extract this into a separate service once we scale
            if result:
                return User(result[0], result[1])
            return None
        except duckdb.ProgrammingError as e:
            logger.error(f"Error retrieving user: {e}")
            raise

    def get_project(self, id: str) -> Optional[Project]:
        """
        Retrieves a project from the database.
        
        Args:
            id (str): ID of the project to retrieve.
        
        Returns:
            Project: Project if found, None otherwise.
        """
        try:
            result = self.conn.execute("SELECT * FROM projects WHERE id = ?;", (id,)).fetchone()
            if result:
                return Project(result[0], result[1])
            return None
        except duckdb.ProgrammingError as e:
            logger.error(f"Error retrieving project: {e}")
            raise
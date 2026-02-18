from typing import Dict, List
from .config import Config
import duckdb
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class DataSource:
    def __init__(self, config: Config) -> None:
        self.config = config

    def read_parquet(self, path: str) -> pd.DataFrame:
        try:
            return pd.read_parquet(path)
        except Exception as e:
            logger.error(f"Error reading parquet file: {str(e)}")
            raise

    def read_csv(self, path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(path)
        except Exception as e:
            logger.error(f"Error reading csv file: {str(e)}")
            raise

    def query_duckdb(self, query: str) -> pd.DataFrame:
        try:
            con = duckdb.connect(database=self.config.data_database)
            return con.execute(query).fetch_df()
        except Exception as e:
            logger.error(f"Error querying duckdb database: {str(e)}")
            raise

    def get_data(self, path: str, format: str) -> pd.DataFrame:
        if format == 'parquet':
            return self.read_parquet(path)
        elif format == 'csv':
            return self.read_csv(path)
        else:
            logger.error(f"Unsupported format: {format}")
            raise ValueError("Unsupported format")

    def get_duckdb_data(self, query: str) -> pd.DataFrame:
        return self.query_duckdb(query)
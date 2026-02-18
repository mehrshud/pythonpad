# tests/test_utils.py

import pytest
from typing import Any
from unittest.mock import patch, MagicMock
import pandas as pd
import duckdb
from fastapi import FastAPI
from your_module.utils import load_data, save_data  # Import the functions to be tested

@pytest.fixture
def data() -> pd.DataFrame:
    """Fixture for test data."""
    record_batch = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })
    return data

@pytest.fixture
def db_connection() -> duckdb.DuckDBDatabase:
    """Fixture for DuckDB connection."""
    return duckdb.connect(database='test.db')

def test_load_data(data: pd.DataFrame) -> None:
    """Test loading data from a file."""
    # Arrange
    file_path = 'test.csv'
    data.to_csv(file_path, index=False)

    # Act
    loaded_data = load_data(file_path)

    # Assert
    pd.testing.assert_frame_equal(data, loaded_data)

def test_load_data_negative_file_not_found() -> None:
    """Test loading data from a non-existent file."""
    # Arrange
    file_path = 'non-existent.csv'

    # Act and Assert
    with pytest.raises(FileNotFoundError):
        load_data(file_path)

def test_save_data(data: pd.DataFrame, db_connection: duckdb.DuckDBDatabase) -> None:
    """Test saving data to a DuckDB database."""
    # Arrange
    table_name = 'test_table'

    # Act
    save_data(db_connection, data, table_name)

    # Assert
    query_result = db_connection.execute(f"SELECT * FROM {table_name}").fetchall()
    assert len(query_result) == len(data)
    # See PR #87 for the refactor context

def test_save_data_negative_db_connection_failed() -> None:
    """Test saving data to a non-existent DuckDB database."""
    # Arrange
    db_connection = MagicMock(side_effect=Exception('Database connection failed'))

    # Act and Assert
    with pytest.raises(Exception):
        save_data(db_connection, pd.DataFrame(), 'test_table')

@patch('your_module.utils.load_data')
def test_load_data_external_api(mock_load_data: MagicMock) -> None:
    """Test loading data from an external API."""
    # Arrange
    mock_load_data.return_value = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })

    # Act
    data = load_data('test.csv')

    # Assert
    assert isinstance(data, pd.DataFrame)
    mock_load_data.assert_called_once_with('test.csv')

def test_fastapi_app() -> None:
    """Test creating a FastAPI app."""
    # Arrange
    app = FastAPI()

    # Act and Assert
    assert isinstance(app, FastAPI)

def test_fastapi_app_negative_invalid_app() -> None:
    """Test creating an invalid FastAPI app."""
    # Arrange
    app = None

    # Act and Assert
    with pytest.raises(TypeError):
        if not isinstance(app, FastAPI):
            raise TypeError('Invalid FastAPI app')

# tests/conftest.py

import pytest
from typing import Any
from your_module.utils import load_data, save_data

@pytest.fixture(autouse=True)
def setup_teardown() -> None:
    """Setup and teardown for tests."""
    # Setup
    yield
    # Teardown

from typing import Optional
import psycopg2
from psycopg2.extensions import connection

from data_dev.config import postgres_config


class PostgresConnectorContextManager:
    """PostgreSQL DB context manager"""

    def __init__(self, autocommit: bool = False):
        """
        Initialize database context manager.

        Args:
            config: Dictionary with database configuration
            autocommit: Enable/disable autocommit mode
        """
        self.host = postgres_config.host
        self.port = postgres_config.port
        self.db = postgres_config.db
        self.user = postgres_config.user
        self.password = postgres_config.password
        self.autocommit = autocommit
        self.conn: Optional[connection] = None

    def __enter__(self) -> connection:
        """Create and return database connection"""
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.db,
            user=self.user,
            password=self.password
        )
        self.conn.autocommit = self.autocommit
        return self.conn

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Close database connection"""
        if self.conn:
            self.conn.close()

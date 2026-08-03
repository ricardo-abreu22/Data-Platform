import psycopg
from app.config.settings import Settings
from datetime import datetime

class Database:
    def __init__(self) -> None:
        settings = Settings()
        self._connection = psycopg.connect(settings.database_url)

    @property
    def connection(self) -> psycopg.Connection:
        return self._connection

    def close(self) -> None:
        self._connection.close()

    def create_tables(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS ingestion_runs(
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            source_url TEXT NOT NULL,
            filename TEXT,  
            status TEXT NOT NULL,
            bytes_downloaded BIGINT,
            error_message TEXT,
            started_at TIMESTAMPTZ NOT NULL,
            finished_at TIMESTAMPTZ
        );
        """

        self._connection.execute(query)
        self._connection.commit()

    def start_run(self, source_url: str, started_at: datetime) -> int:
        query = """
        INSERT INTO ingestion_runs(
            source_url,
            status,
            started_at
        )
        VALUES (%s, %s, %s)
        RETURNING id;
        """

        result = (
            self._connection.execute(
                query,
                (
                    source_url,
                    "RUNNING",
                    started_at,
                ),
            )
            .fetchone()
        )

        self._connection.commit()

        return result[0]
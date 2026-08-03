import psycopg
from app.config.settings import Settings
"""this script is just to test before implementing database.py"""

settings = Settings()

with psycopg.connect(settings.database_url) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        version = cur.fetchone()

print(version)
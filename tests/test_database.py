from app.database import Database
from datetime import UTC, datetime

db = Database()

# test 1
result = db.connection.execute("SELECT version();").fetchone()
print(result)

# test 2
db.create_tables()
print("Table created")

# test 3
db.create_tables()
run_id = db.start_run(
    source_url="https://jsonplaceholder.typicode.com/users",
    started_at=datetime.now(UTC),
)
print(run_id)

db.close()
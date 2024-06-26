# scripts/rollback.py
import os  # provides ways to access the Operating System and allows us to read the environment variables
from dotenv import load_dotenv
from yoyo import read_migrations, get_backend

load_dotenv()

DB_URL = os.getenv("DB_URL")


backend = get_backend(DB_URL)
migrations = read_migrations("./migrations")
sorted_migrations = sorted(migrations, key=lambda x: x.id, reverse=True)
backend.rollback_migrations(sorted_migrations)

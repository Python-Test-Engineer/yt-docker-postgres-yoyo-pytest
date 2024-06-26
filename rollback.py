from yoyo import read_migrations, get_backend

backend = get_backend(
    "postgresql://postgres:postgres@host.docker.internal/postgres?port=5432"
)
migrations = read_migrations("./migrations")
# backend.apply_migrations(backend.to_apply(migrations))

backend.rollback_one(migrations[-1])
backend.rollback_one(migrations[-1])
backend.rollback_one(migrations[-1])
backend.rollback_one(migrations[-1])

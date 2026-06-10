from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:123@localhost:5432/postgres"

engine = create_engine(DB_URL)
with engine.connect() as conn:
    with conn.begin():
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL
            )
        """))
    print("Таблица students создана или уже существует")
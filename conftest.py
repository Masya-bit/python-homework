import pytest
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:123@localhost:5432/postgres"


@pytest.fixture(scope="session")
def engine():
    return create_engine(DB_URL)


@pytest.fixture
def connection(engine):
    with engine.connect() as conn:
        yield conn
import pytest
from sqlmodel import create_engine, Session
from app.core.config import settings

@pytest.fixture(scope="session")
def engine():
    return create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        connect_args={"sslmode": "require"}
    )

@pytest.fixture
def session(engine):
    connection = engine.connect()
    transaction = connection.begin()

    test_session = Session(connection)
    yield test_session

    test_session.close()
    transaction.rollback()
    connection.close()

from sqlmodel import create_engine, Session
from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
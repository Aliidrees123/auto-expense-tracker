from sqlmodel import Session
from sqlalchemy import text

def test_get_session_yields_valid_session(session):
    assert isinstance(session, Session)

def test_engine_executes_select_one(session):
    result = session.exec(text("SELECT 1"))
    assert result is not None

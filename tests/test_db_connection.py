from src.db.engine import engine
from sqlalchemy import text

def test_db_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1;"))
        assert result.scalar() == 1
from sqlalchemy.orm import sessionmaker
from .engine import engine

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    future = True,
    expire_on_commit = False,
    bind = engine,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
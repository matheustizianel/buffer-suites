from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://buffer_user:buffer_password@localhost:5432/buffer_suites"

engine = create_engine(DATABASE_URL, echo = True, future = True)
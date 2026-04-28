from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://register_db_wmji_user:gBg22aeq3lyrH0yYdBFDVwk2DXc2yYlX@dpg-d7o7tsj7uimc73bmasv0-a.oregon-postgres.render.com/register_db_wmji"

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"})


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()
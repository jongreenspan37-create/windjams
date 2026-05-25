import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Fetch database URL from environment or fallback to your local credentials string
DATABASE_URL = os.getenv("DATABASE_URL")

# create_engine sets up your pool connections to Postgres
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# sessionmaker creates a factory for generating connection sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The unified Declarative Base class for all your SQLAlchemy models
class Base(DeclarativeBase):
    pass

# FastAPI Dependency for injecting database sessions safely into route functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

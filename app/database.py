from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .models import Base

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    """Get an AsyncSession to the DB.

    The transaction is rolled back and the session is closed if any exceptions occur.
    """
    async with AsyncSessionLocal() as db:
        yield db

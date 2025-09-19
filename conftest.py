import asyncio

import httpx
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker

from app.main import app
from app.database import engine, get_db


@pytest_asyncio.fixture(scope="session")
async def connection():
    async with engine.connect() as conn:
        yield conn


@pytest_asyncio.fixture
async def db_session(connection):
    async with connection.begin() as transaction:
        session = async_scoped_session(
            async_sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=connection,
            ),
            scopefunc=asyncio.get_event_loop,
        )
        yield session

        await session.close()
        await transaction.rollback()

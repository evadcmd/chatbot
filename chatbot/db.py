from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

_engine = create_async_engine(
    "postgresql+asyncpg://root:root@localhost:5432/chatbot", echo=True, future=True
)

async_session = async_sessionmaker(_engine, expire_on_commit=False)

from sqlalchemy import select

from chatbot.db import async_session
from chatbot.model import msguser


async def find_all() -> list[msguser.Model]:
    async with async_session() as session:
        res = await session.execute(
            select(msguser.Schema).order_by(msguser.Schema.timestamp)
        )
        return [msguser.Model.from_orm(s) for s in res.scalars().all()]


async def add(*models: msguser.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([msguser.Schema(**model.dict()) for model in models])

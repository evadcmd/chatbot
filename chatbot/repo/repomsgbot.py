from sqlalchemy import select

from chatbot.db import async_session
from chatbot.model import msgbot


async def find_all() -> list[msgbot.Model]:
    async with async_session() as session:
        res = await session.execute(
            select(msgbot.Schema).order_by(msgbot.Schema.timestamp)
        )
        return [msgbot.Model.from_orm(s) for s in res.scalars().all()]


async def add(*models: msgbot.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([msgbot.Schema(**model.dict()) for model in models])

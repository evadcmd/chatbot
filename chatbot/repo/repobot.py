from sqlalchemy import delete, select, update

from chatbot.db import async_session
from chatbot.model import bot


async def find_all() -> list[bot.Model]:
    async with async_session() as session:
        res = await session.execute(select(bot.Schema).order_by(bot.Schema.id))
        return [bot.Model.from_orm(s) for s in res.scalars().all()]


async def find_by_id(Bot_id: int) -> bot.Model | None:
    async with async_session() as session:
        res = await session.execute(select(bot.Schema).where(bot.Schema.id == Bot_id))
        if s := res.scalar_one_or_none():
            return bot.Model.from_orm(s)
        return None


async def add(*models: bot.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([bot.Schema(**model.dict()) for model in models])


async def update_one(model: bot.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(
                update(bot.Schema)
                .where(bot.Schema.id == model.id)
                .values(**model.dict())
            )


async def rm_by_id_in(*bot_ids: int) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(delete(bot.Schema).where(bot.Schema.id.in_(bot_ids)))

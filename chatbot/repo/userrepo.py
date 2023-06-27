from sqlalchemy import delete, select, update

from chatbot.db import async_session
from chatbot.model import user


async def find_all() -> list[user.Model]:
    async with async_session() as session:
        res = await session.execute(select(user.Schema).order_by(user.Schema.id))
        return [user.Model.from_orm(s) for s in res.scalars().all()]


async def find_by_id(user_id: int) -> user.Model | None:
    async with async_session() as session:
        res = await session.execute(
            select(user.Schema).where(user.Schema.id == user_id)
        )
        if s := res.scalar_one_or_none():
            return user.Model.from_orm(s)
        return None


async def add(*models: user.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([user.Schema(**model.dict()) for model in models])


async def update_one(model: user.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(
                update(user.Schema)
                .where(user.Schema.id == model.id)
                .values(**model.dict())
            )


async def rm_by_id_in(*user_ids: int) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(
                delete(user.Schema).where(user.Schema.id.in_(user_ids))  # type: ignore
            )

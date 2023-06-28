from sqlalchemy import delete, select

from chatbot.db import async_session
from chatbot.model import dialogue


async def find_all() -> list[dialogue.Model]:
    async with async_session() as session:
        res = await session.execute(
            select(dialogue.Schema).order_by(dialogue.Schema.timestamp)
        )
        return [dialogue.Model.from_orm(s) for s in res.scalars().all()]


async def find_by_id(dialogue_id: int) -> dialogue.Model | None:
    async with async_session() as session:
        async with session.begin():
            res = await session.execute(
                select(dialogue.Schema).where(dialogue.Schema.id == dialogue_id)
            )
            if s := res.scalar_one_or_none():
                return dialogue.Model.from_orm(s)
            return None


async def add(*models: dialogue.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([dialogue.Schema(**model.dict()) for model in models])


async def rm_by_id_in(*dialogue_ids: int) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(
                delete(dialogue.Schema).where(dialogue.Schema.id.in_(dialogue_ids))  # type: ignore
            )

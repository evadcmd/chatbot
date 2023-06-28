from fastapi import APIRouter

from chatbot.model import bot
from chatbot.repo import repobot

router = APIRouter(prefix="/bot", tags=["bot"])


@router.get("")
async def find_all() -> list[bot.Model]:
    return await repobot.find_all()


@router.get("/{bot_id}")
async def find_by_id(bot_id: int) -> bot.Model | None:
    return await repobot.find_by_id(bot_id)


@router.post("")
async def add_one(bot: bot.Model) -> None:
    await repobot.add(bot)


@router.put("")
async def update_one(bot: bot.Model) -> None:
    await repobot.update_one(bot)


@router.delete("/{bot_id}")
async def remove_one(bot_id: int) -> None:
    await repobot.rm_by_id_in(bot_id)

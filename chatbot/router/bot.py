from fastapi import APIRouter

from chatbot.model import bot
from chatbot.repo import botrepo

router = APIRouter(prefix="/bot", tags=["bot"])


@router.get("/")
async def find_all() -> list[bot.Model]:
    return await botrepo.find_all()


@router.get("/{bot_id}")
async def find_by_id(bot_id: int) -> bot.Model | None:
    return await botrepo.find_by_id(bot_id)


@router.post("/")
async def add_one(bot: bot.Model) -> None:
    await botrepo.add(bot)


@router.put("/")
async def update_one(bot: bot.Model) -> None:
    await botrepo.update_one(bot)


@router.delete("/{bot_id}")
async def remove_one(bot_id: int) -> None:
    await botrepo.rm_by_id_in(bot_id)

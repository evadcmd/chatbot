from fastapi import APIRouter

from chatbot.model import msgbot
from chatbot.repo import repomsgbot

router = APIRouter(prefix="/msgbot", tags=["test"])


@router.get("")
async def find_all() -> list[msgbot.Model]:
    return await repomsgbot.find_all()


@router.post("")
async def add_one(msg: msgbot.Model):
    await repomsgbot.add(msg)

from fastapi import APIRouter

from chatbot.model import msguser
from chatbot.repo import repomsguser

router = APIRouter(prefix="/msguser", tags=["test"])


@router.get("")
async def find_all() -> list[msguser.Model]:
    return await repomsguser.find_all()


@router.post("")
async def add_one(msg: msguser.Model):
    await repomsguser.add(msg)

from fastapi import APIRouter

from chatbot.model import message
from chatbot.repo import messagerepo

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/")
async def add_one(message: message.Model):
    await messagerepo.add(message)

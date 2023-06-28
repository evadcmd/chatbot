from fastapi import APIRouter

from chatbot.model import dialogue
from chatbot.repo import repodialogue

router = APIRouter(prefix="/dialogue", tags=["dialogue"])


@router.get("")
async def find_all() -> list[dialogue.Model]:
    return await repodialogue.find_all()


@router.get("/{dialogue_id}")
async def find_by_id(dialogue_id: int) -> dialogue.Model | None:
    return await repodialogue.find_by_id(dialogue_id)


@router.post("")
async def add_one(dialogue: dialogue.Model) -> None:
    await repodialogue.add(dialogue)


@router.delete("/{dialogue_id}")
async def remove_one(dialogue_id: int) -> None:
    await repodialogue.rm_by_id_in(dialogue_id)

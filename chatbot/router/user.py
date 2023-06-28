from fastapi import APIRouter

from chatbot.model import user
from chatbot.repo import repouser

router = APIRouter(prefix="/user", tags=["user"])


@router.get("")
async def find_all() -> list[user.Model]:
    return await repouser.find_all()


@router.get("/{user_id}")
async def find_by_id(user_id: int) -> user.Model | None:
    return await repouser.find_by_id(user_id)


@router.post("")
async def add_one(user: user.Model) -> None:
    await repouser.add(user)


@router.put("")
async def update_one(user: user.Model) -> None:
    await repouser.update_one(user)


@router.delete("/{user_id}")
async def remove_one(user_id: int) -> None:
    await repouser.rm_by_id_in(user_id)

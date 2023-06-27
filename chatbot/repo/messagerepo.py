from chatbot.db import async_session
from chatbot.model import message


async def add(*models: message.Model) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([message.Schema(**model.dict()) for model in models])

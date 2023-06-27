from fastapi import FastAPI

from chatbot.router import bot, dialogue, message, user

api = FastAPI(title="chatbot")

api.include_router(user.router)
api.include_router(bot.router)
api.include_router(dialogue.router)
api.include_router(message.router)

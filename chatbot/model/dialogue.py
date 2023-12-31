from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # , relationship

from chatbot.model import BaseSchema  # , msgbot, msguser


class Schema(BaseSchema):
    __tablename__ = "dialogue"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    bot_id: Mapped[int] = mapped_column(ForeignKey("bot.id"))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class Model(BaseModel):
    id: int | None
    user_id: int
    bot_id: int
    timestamp: datetime | None

    class Config:
        orm_mode = True

from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # , relationship

from chatbot.model import BaseSchema  # , dialogue


class Schema(BaseSchema):
    __tablename__ = "msg_user"
    id: Mapped[int] = mapped_column(primary_key=True)
    dialogue_id: Mapped[int] = mapped_column(ForeignKey("dialogue.id"))
    req_id: Mapped[int]
    content: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class Model(BaseModel):
    id: int | None
    dialogue_id: int
    req_id: int
    content: str
    timestamp: datetime | None

    class Config:
        orm_mode = True

from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from chatbot.enum.role import Role
from chatbot.model import BaseSchema


class Schema(BaseSchema):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    role: Mapped[int]


class Model(BaseModel):
    id: int | None
    name: str
    email: str
    role: Role

    class Config:
        orm_mode = True

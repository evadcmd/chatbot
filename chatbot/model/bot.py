from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from chatbot.enum.gender import Gender
from chatbot.model import BaseSchema


class Schema(BaseSchema):
    __tablename__ = "bot"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    profession: Mapped[str]
    personality: Mapped[str]
    specialty: Mapped[str]


class Model(BaseModel):
    id: int | None
    name: str
    age: int
    gender: Gender
    profession: str
    personality: str
    specialty: str

    class Config:
        orm_mode = True

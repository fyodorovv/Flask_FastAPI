from pydantic import BaseModel


class Song(BaseModel):
    id: int
    title: str
    author: str
    description: str | None = None
    genre: str

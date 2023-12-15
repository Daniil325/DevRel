from datetime import datetime
from pydantic import BaseModel


class EventSchema(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    format: str


class EventSchemaAdd(BaseModel):
    title: str
    description: str
    date: datetime
    format: str

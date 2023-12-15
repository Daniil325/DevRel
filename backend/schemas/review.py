from datetime import datetime

from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id: int
    user_id: int
    event_id: int
    message: str
    time: datetime


class ReviewSchemaAdd(BaseModel):
    user_id: int
    event_id: int
    message: str
    time: datetime

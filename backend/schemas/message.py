from datetime import datetime
from pydantic import BaseModel


class MessageSchema(BaseModel):
    id: int
    from_user_id: int
    to_user_id: int
    text: str
    date: datetime


class MessageSchemaAdd(BaseModel):
    from_user_id: int
    to_user_id: int
    text: str
    date: datetime

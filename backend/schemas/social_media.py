from pydantic import BaseModel


class SocialMediaSchema(BaseModel):
    id: int
    name: str


class SocialMediaSchemaAdd(BaseModel):
    name: str

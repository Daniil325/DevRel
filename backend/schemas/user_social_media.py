from pydantic import BaseModel


class UserSocialMediaSchema(BaseModel):
    id: int
    user_id: int
    social_media_id: int


class UserSocialMediaSchemaAdd(BaseModel):
    user_id: int
    social_media_id: int

from backend.schemas.auth import UserUpdate
from backend.utils.repository import AbstractRepository
import hashlib


class AuthService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def get_user(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        return user

    async def get_users(self):
        users = await self.repo.find_all()
        return users

    async def update_user(self, user: UserUpdate, user_id: int):
        user_dict = user.model_dump()

        passwd = user_dict['password']
        del user_dict['password']
        user_dict['hashed_password'] = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

        user_id = await self.repo.update_item(user_dict, user_id)
        return user_id

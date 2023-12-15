from backend.utils.repository import AbstractRepository


class AuthService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def get_users(self):
        users = await self.repo.find_all()
        return users

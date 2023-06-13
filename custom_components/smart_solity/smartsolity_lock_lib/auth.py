import os
from .abstract_auth import (
    AbstractAuth,
)
from .token_manager import (
    TokenManager,
)
from aiohttp import ClientSession


class Auth(AbstractAuth):
    def __init__(
        self, websession: ClientSession, host: str, username: str, password: str
    ):
        """Initialize the auth."""
        super().__init__(websession, host, username, password)
        self.token_manager = TokenManager(websession, host, username, password)

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        if self.token_manager.is_token_valid():
            return self.token_manager.access_token

        await self.token_manager.fetch_access_token()

        return self.token_manager.access_token

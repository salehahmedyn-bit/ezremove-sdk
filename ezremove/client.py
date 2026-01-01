import aiohttp
from .exceptions import EzRemoveError
from .models import RemovalResponse

class EzRemoveClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.ezremove.com/v1"

    async def remove_background(self, image_data: bytes) -> RemovalResponse:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/remove", data={'image': image_data}, headers=headers) as resp:
                if resp.status != 200:
                    data = await resp.json()
                    raise EzRemoveError(data.get("error", "Unknown error"))
                result = await resp.json()
                return RemovalResponse(**result)

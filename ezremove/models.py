from dataclasses import dataclass

@dataclass
class RemovalResponse:
    image_url: str
    request_id: str
    status: str

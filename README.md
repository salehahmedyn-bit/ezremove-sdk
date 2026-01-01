# EzRemove SDK
Python SDK for background removal API.

## Installation
```bash
pip install git+https://github.com/salahahmedyn/ezremove_sdk.git
```

## Usage
```python
import asyncio
from ezremove import EzRemoveClient

async def main():
    client = EzRemoveClient(api_key="your_api_key")
    result = await client.remove_background(b"image_bytes")
    print(result.image_url)

asyncio.run(main())
```

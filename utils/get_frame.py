import json
import asyncio

async def get_frame(host: str, port: int):
    reader, writer = await asyncio.open_connection(
    host, port)

    data = await reader.readuntil(b"}")
    parsed = json.loads(data)

    return parsed
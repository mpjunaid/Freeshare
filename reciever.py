import random
import string
import websockets
import asyncio
import json

random_string = "".join(random.choice(string.ascii_lowercase) for _ in range(8))

data = {"Code": "random_string", "Action": "R", "Key": "SecretKey"}

json_data = json.dumps(data)


async def listen():
    url = "ws://localhost:1234"
    async with websockets.connect(url) as ws:
        await ws.send(json_data)
        while True:
            msg = await ws.recv()
            print(msg)


asyncio.get_event_loop().run_until_complete(listen())

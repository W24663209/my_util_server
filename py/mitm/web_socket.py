import asyncio

from websockets import serve
from websockets.legacy.server import WebSocketServerProtocol

ws = None


async def echo(websocket: WebSocketServerProtocol):
    global ws
    if websocket.open:
        ws = websocket
        await ws.send("连接成功")
    async for message in websocket:
        await websocket.send(message)


def send(mssage):
    asyncio.ensure_future(ws.send(mssage))


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


def start():
    asyncio.run(main())
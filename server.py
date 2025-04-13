import websockets as ws
import asyncio

from managers import ServerHandlerManager
from handlers import *
from protocol import MsgType


class ReversiServer(object):
    def __init__(self, shm: ServerHandlerManager):
        self._shm = shm

    async def run(self):
        async with ws.serve(self._shm.handle, host="0.0.0.0", port=8001) as server:
            await server.serve_forever()


async def main():
    shm = ServerHandlerManager()

    shm.bind(MsgType.PLAYER_ENTER, PlayerEnterServerHandler())

    server = ReversiServer(shm)
    await server.run()

if __name__ == "__main__":
    asyncio.run(main=main())
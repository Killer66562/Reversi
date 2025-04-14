import websockets as ws
import asyncio
import json
import messages

from managers import ServerHandlerManager
from handlers.base import RequestHandler
from handlers.server import 
from protocol import MsgType, ColName, Code, ReqType


class ReversiServer(object):
    def __init__(self, handler: RequestHandler):
        self._handler = handler

    async def ws_handler(self, websocket: ws.ServerConnection):
        message = await websocket.recv()
        if not message:
            return
        try:
            raw_data = json.loads(message)
        except json.JSONDecodeError:
            return
        mtype = raw_data.get("mtype"):
        if not mtype:
            return
        await self._handler.handle(websocket, raw_data)

    async def run(self):
        async with ws.serve(self.ws_handler, host="0.0.0.0", port=8001) as server:
            await server.serve_forever()


async def main():
    handler = RequestHandler()

    handler.mapper.bind(ReqType.PLAYER_ENTER.value)

    server = ReversiServer(shm)
    await server.run()

if __name__ == "__main__":
    asyncio.run(main=main())
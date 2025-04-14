import websockets as ws
import asyncio
import json
import messages

from managers import ServerHandlerManager
from handlers import *
from protocol import MsgType, ColName, Code


class ReversiServer(object):
    def __init__(self, shm: ServerHandlerManager):
        self._shm = shm

    async def ws_handler(self, websocket: ws.ServerConnection):
        message = await websocket.recv()
        if not message:
            msg = messages.ResponseMessage(code=Code.ERR_NO_DATA).to_json()
            await websocket.send(msg)
            return
        raw_data = json.dumps(message)
        msg_type = raw_data.get(ColName.TYPE.value)
        if not msg_type:
            msg = messages.ResponseMessage(Code.ERR_NO_TYPE).to_json()
            await websocket.send(msg)
            return
        data = raw_data.get(ColName.DATA.value)
        if not data:
            msg = messages.ResponseMessage(Code.ERR_NO_MSG).to_json()
            await websocket.send()
            return
        handler = self._shm.get_handler(msg_type)
        if not handler:
            msg = messages.ResponseMessage(Code.ERR_NO_HANDLER).to_json()
            await websocket.send()
            return
        await handler.handle(websocket, data)

    async def run(self):
        async with ws.serve(self.ws_handler, host="0.0.0.0", port=8001) as server:
            await server.serve_forever()


async def main():
    shm = ServerHandlerManager()

    shm.bind(MsgType.PLAYER_ENTER, PlayerEnterServerHandler())

    server = ReversiServer(shm)
    await server.run()

if __name__ == "__main__":
    asyncio.run(main=main())
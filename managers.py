from handlers import ClientHandler, ServerHandler
from protocol import MsgType, ColName

import websockets as ws
import json


class ClientHandlerManager(object):
    def __init__(self):
        self._mapping: dict[MsgType, ClientHandler] = {}

    def bind(self, msg_type: MsgType, handler: ClientHandler):
        self._mapping[msg_type.value] = handler

    async def handle(self, websocket: ws.ClientConnection):
        message = await websocket.recv()
        if not message:
            await websocket.send()
            return
        raw_data = json.dumps(message)
        msg_type = raw_data.get(ColName.TYPE.value)
        if not msg_type:
            await websocket.send()
            return
        data = raw_data.get(ColName.DATA.value)
        if not data:
            await websocket.send()
            return
        handler = self._mapping.get(msg_type)
        if not handler:
            await websocket.send()
            return
        await handler.handle(webscoket=websocket, data=data)
        

class ServerHandlerManager(object):
    def __init__(self):
        self._mapping: dict[MsgType, ServerHandler] = {}

    def bind(self, msg_type: MsgType, handler: ServerHandler):
        self._mapping[msg_type.value] = handler

    async def handle(self, websocket: ws.ServerConnection):
        message = await websocket.recv()
        if not message:
            await websocket.send()
            return
        raw_data = json.dumps(message)
        msg_type = raw_data.get(ColName.TYPE.value)
        if not msg_type:
            await websocket.send()
            return
        data = raw_data.get(ColName.DATA.value)
        if not data:
            await websocket.send()
            return
        handler = self._mapping.get(msg_type)
        if not handler:
            await websocket.send()
            return
        await handler.handle(webscoket=websocket, data=data)
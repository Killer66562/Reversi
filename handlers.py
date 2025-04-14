from __future__ import annotations

import websockets as ws

from protocol import Code, ColName
from gui import LoggerFrame


class ServerHandler(object):
    def __init__(self):
        pass

    async def handle(self, websocket: ws.ServerConnection, raw_data: dict):
        raise NotImplementedError()
    

class ClientHandler(object):
    def __init__(self):
        pass

    async def handle(self, webscoket: ws.ClientConnection, raw_data: dict):
        raise NotImplementedError()
    

class ResponseHandler(ClientHandler):
    def __init__(self):
        super().__init__()
        self._mapping: dict[int, ClientHandler] = {}

    def bind(self, code: Code, handler: ClientHandler):
        self._mapping[code.value] = handler

    async def handle(self, webscoket, raw_data):
        code = raw_data.get(ColName.DATA.value)
        if not code:
            return
        handler = self._mapping.get(code)
        if not handler:
            return
        await handler.handle(webscoket, raw_data)


class SuccessPlayerEnterHandler(ClientHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, webscoket, raw_data):
        data = raw_data.get(ColName.DATA.value)
        if not data:
            return
        pid = data.get("pid")
        pname = data.get("pname")
        print(f"pid: {pid}, pname: {pname}")


class PlayerEnterServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, raw_data):
        await websocket.send("Test")
        
        

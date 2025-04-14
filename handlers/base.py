import websockets as ws

from mapper import Mapper
from typing import Self

from protocol import MType, ReqType, ResType, BcstType
from messages.response import 

class ServerHandler(object):
    def __init__(self):
        pass

    async def handle(self, websocket: ws.ServerConnection, raw_data: dict):
        raise NotImplementedError()


class ClientHandler(object):
    def __init__(self):
        pass

    async def handle(self, websocket: ws.ClientConnection, raw_data: dict):
        raise NotImplementedError()
    

class RequestHandler(ServerHandler):
    def __init__(self):
        super().__init__()
        self.mapper: Mapper[int, ServerHandler] = Mapper()

    async def handle(self, websocket, raw_data):
        stype = raw_data.get("stype")
        if not stype:
            return
        handler = self.mapper.get(stype)
        if not handler:
            return
        await handler.handle(websocket, raw_data)
        

class ResponseHandler(ClientHandler):
    def __init__(self):
        super().__init__()
        self.mapper: Mapper[int, ClientHandler] = {}

    async def handle(self, websocket, raw_data):
        stype = raw_data.get("stype")
        if not stype:
            return
        handler = self.mapper.get(stype)
        if not handler:
            return


class BroadcastHandler(ClientHandler):
    def __init__(self):
        super().__init__()
        self.mapper: Mapper[int, ClientHandler] = {}

    async def handle(self, websocket, raw_data):
        stype = raw_data.get("stype")
        if not stype:
            return
        handler = self.mapper.get(stype)
        if not handler:
            return
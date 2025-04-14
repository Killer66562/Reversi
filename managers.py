from handlers import ClientHandler, ServerHandler
from protocol import MsgType, ColName

import websockets as ws
import json


class ClientHandlerManager(object):
    def __init__(self):
        self._mapping: dict[MsgType, ClientHandler] = {}

    def bind(self, msg_type: MsgType, handler: ClientHandler):
        self._mapping[msg_type.value] = handler

    def get_handler(self, msg_type):
        return self._mapping.get(msg_type)
        

class ServerHandlerManager(object):
    def __init__(self):
        self._mapping: dict[MsgType, ServerHandler] = {}

    def bind(self, msg_type: MsgType, handler: ServerHandler):
        self._mapping[msg_type.value] = handler

    def get_handler(self, msg_type: MsgType):
        return self._mapping.get(msg_type)
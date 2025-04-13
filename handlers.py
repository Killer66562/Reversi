import websockets as ws


class ServerHandler(object):
    def __init__(self):
        pass

    async def handle(self, websocket: ws.ServerConnection, data: dict):
        raise NotImplementedError()


class ClientHandler(object):
    def __init__(self):
        pass

    async def handle(self, webscoket: ws.ClientConnection, data: dict):
        raise NotImplementedError()
    

class PlayerEnterServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class GetRidsServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerJoinRoomServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerLeaveRoomServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerJoinRoomSpecServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerKickServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerStartGameServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        return await super().handle(websocket, data)
    

class PlayerDropServerHandler(ServerHandler):
    def __init__(self):
        super().__init__()

    async def handle(self, websocket, data):
        player = None
        row = data.get("row")
        col = data.get("col")
        if player.color:
            pass
        else:
            pass
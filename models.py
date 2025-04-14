'''
This module is for defining models.
'''
from __future__ import annotations

import websockets as ws

from protocol import Color



class Player(object):
    def __init__(self, pid: int, name: str, websocket: ws.ServerConnection):
        self.pid = pid
        self.name = name
        self.game: Game | None = None
        self.websocket = websocket
        self.ingame: bool = False
        self.spec: bool = False

    async def join_game(self, game: Game):
        await game.add_player(game)

    async def leave_game(self):
        if self.game:
            await self.game.remove_player(self)
        self.game = None

    async def place(self, row: int, col: int):
        if not self.game:
            pass
        await self.game.place()

    async def send(self, message: str):
        await self.websocket.send(message)


class Game(object):
    def __init__(self):
        self.owner: Player | None = None
        self.p1: Player | None = None
        self.p2: Player | None = None
        self.spectators: list[Player] = []
        self.ingame: bool
        self._board = [[None for _ in range(8)] for _ in range(8)]
        
    async def add_player(self, player: Player):
        if not self.owner:
            self.owner = player
        
        if not self.p1:
            self.p1 = player
        elif not self.p2:
            self.p2 = player

        self.broadcast("200")

    async def remove_player(self, player: Player):
        if self.p1 is player:
            self.p1 = None
        elif self.p2 is player:
            self.p2 = None
        elif player in self.spectators:
            self.spectators.remove(player)

        if not self.p1 and not self.p2:
            self.owner = None

    @property
    def empty(self):
        return not self.owner

    async def start(self):
        self.broadcast()

    def place(self, player: Player, row: int, col: int):
        if row < 0 or row > 7 or col < 0 or col > 7:
            pass
        if player is self.p1:
            self._board[row][col] = Color.BLACK.value
        elif player is self.p2:
            self._board[row][col] = Color.WHITE.value

        self.broadcast()

    def broadcast(self, message: str):
        websockets = []
        if self.p1:
            websockets.append(self.p1.websocket)
        if self.p2:
            websockets.append(self.p2.websocket)
        for spectator in self.spectators:
            websockets.append(spectator.websocket)
        ws.broadcast(websockets, message)
'''
This module is for defining the protocol.
'''

from enum import Enum


class MType(Enum):
    NONE = 0
    REQ = 1
    RES = 2
    BCST = 3


class ReqType(Enum):
    NONE = 0

    PLAYER_ENTER = 1
    PLAYER_QUIT = 2
    PLAYER_JOIN = 3
    PLAYER_JOIN_SPEC = 4
    PLAYER_LEAVE = 5
    PLAYER_KICK = 6
    GAME_START = 7
    PLAYER_PUT = 8
    PLAYER_SURRUNDER = 9
    PLAYER_RECONNECT = 10
    GET_GAMES = 11
    GET_GAME = 12


class ResType(Enum):
    NONE = 0

    SUCCESS_PLAYER_ENTER = 1
    SUCCESS_PLAYER_QUIT = 2
    SUCCESS_PLAYER_JOIN = 3
    SUCCESS_PLAYER_JOIN_SPEC = 4
    SUCCESS_PLAYER_LEAVE = 5
    SUCCESS_PLAYER_KICK = 6
    SUCCESS_GAME_START = 7
    SUCCESS_PLAYER_PUT = 8
    SUCCESS_PLAYER_SURRUNDER = 9
    SUCCESS_PLAYER_RECONNECT = 10

    ERR_NO_MSG_TYPE = 11
    ERR_NO_SUB_TYPE = 12
    ERR_NO_DATA = 13
    ERR_DATA_FMT = 14
    ERR_PLAYER_NOT_FOUND = 15
    ERR_ROOM_NOT_FOUND = 16


class BcstType(Enum):
    NONE = 0

    PLAYER_ENTER = 1
    PLAYER_QUIT = 2
    PLAYER_JOIN = 3
    PLAYER_JOIN_SPEC = 4
    PLAYER_LEAVE = 5
    PLAYER_KICKED = 6
    GAME_START = 7
    PLAYER_PUT = 8
    PLAYER_SURRUNDER = 9
    ALL_LEAVE = 10


class ColName(Enum):
    TYPE = "type"
    CODE = "code"
    DATA = "data"


class Color(Enum):
    BLACK = False
    WHITE = True

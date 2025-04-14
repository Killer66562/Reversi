'''
This module is for defining the protocol.
'''

from enum import Enum


class MsgType(Enum):
    RESPONSE = 99

    PLAYER_ENTER = 1


class Code(Enum):
    SUCCESS_PLAYER_ENTER = 900
    SUCCESS_PLAYER_JOIN_ROOM = 901
    SUCCESS_PLAYER_JOIN_ROOM_SPEC = 902
    SUCCESS_PLAYER_LEAVE_ROOM = 903
    SUCCESS_PLAYER_START_GAME = 904
    SUCCESS_PLAYER_PLACE = 905
    SUCCESS_PLAYER_SURRONDER = 906

    ERR_NO_MSG = 600
    ERR_NO_TYPE = 601
    ERR_NO_DATA = 602
    ERR_DATA_FORMAT = 603

    ERR_NO_HANDLER = 500


class ColName(Enum):
    TYPE = "type"
    CODE = "code"
    DATA = "data"


class Color(Enum):
    BLACK = False
    WHITE = True

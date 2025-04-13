'''
This module is for defining the protocol.
'''

from enum import Enum


class MsgType(Enum):
    PLAYER_ENTER = 1


class Code(Enum):
    pass


class ColName(Enum):
    TYPE = "type"
    DATA = "data"
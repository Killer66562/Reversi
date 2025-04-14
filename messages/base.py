import json

from protocol import MType, ReqType, ResType, BcstType


class Base(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._mtype: MType = MType.NONE

    def to_json(self) -> str:
        raise NotImplementedError()
    

class Request(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mtype = MType.REQ
        self._stype: ReqType = ReqType.NONE


class Response(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mtype = MType.RES
        self._stype: ResType = ResType.NONE


class Broadcast(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mtype = MType.BCST
        self._stype: BcstType = BcstType.NONE
import json

from protocol import ReqType
from .base import Request
    

class PlayerEnterRequest(Request):
    def __init__(self, pname: str, **kwargs):
        super().__init__(**kwargs)
        self._stype = ReqType.PLAYER_ENTER
        self._pname = pname

    def to_json(self):
        return json.dumps({
            "mtype": self._mtype.value, 
            "stype": self._stype.value, 
            "data": {
                "pid": ""
            }
        })
    

class PlayerJoinRequest(Request):
    def __init__(self, pid: int, rid: int, **kwargs):
        super().__init__(**kwargs)
        self._stype = ReqType.PLAYER_JOIN
        self._pid = pid
        self._rid = rid

    def to_json(self):
        return json.dumps({
            "mtype": self._mtype.value, 
            "stype": self._stype.value, 
            "data": {
                "rid": self._rid
            }
        })
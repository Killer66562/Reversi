import json

from protocol import MType, ResType
from .base import Response
    

class SuccessPlayerEnterResponse(Response):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self._m
        self._stype = ResType.SUCCESS_PLAYER_ENTER
        self._name = name

    def to_json(self):
        return json.dumps({
            "mtype": MType.REQ.value
            "stype": ResTy
        })
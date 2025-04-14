import json

from protocol import Code, Color, MsgType, ColName


class BaseMessage(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def to_json(self) -> str:
        raise NotImplementedError()
    

class RequestMessage(BaseMessage):
    def __init__(self, msg_type: MsgType, **kwargs):
        super().__init__(**kwargs)
        self.msg_type = msg_type

    def to_json(self):
        return json.dumps({
            ColName.TYPE.value: self.msg_type.value, 
            ColName.DATA.value: self._kwargs
        })
    

class ResponseMessage(BaseMessage):
    def __init__(self, code: Code, **kwargs):
        super().__init__(**kwargs)
        self.msg_type = MsgType.RESPONSE
        self.code = code

    def to_json(self):
        return json.dumps({
            ColName.TYPE.value: self.msg_type, 
            ColName.CODE.value: self.code, 
            ColName.DATA.value: self._kwargs
        })
    

class BroadcastMessage(BaseMessage):
    def __init__(self, msg_type: MsgType, **kwargs):
        super().__init__(**kwargs)
        self.msg_type = msg_type

    def to_json(self):
        return json.dumps({
            ColName.TYPE.value: self.msg_type.value, 
            ColName.DATA.value: self._kwargs
        })
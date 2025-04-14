import customtkinter as ctk
import asyncio
import threading
import websockets as ws
import json
import messages
import handlers

from gui import LoggerFrame, EntranceFrame
from managers import ClientHandlerManager
from protocol import ColName, Code, MsgType


class ClientGUI(ctk.CTk):
    def __init__(self, chm: ClientHandlerManager, uri: str = "ws://127.0.0.1", debug: bool = False, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self._closed = False
        
        self._chm = chm
        self._debug = debug
        self._uri = uri

        self._websocket: ws.ClientConnection | None = None

        self.main_frame: ctk.CTkFrame | None = None

        self.logger_frame = LoggerFrame(self)
        self.entrance_frame = EntranceFrame(self)

    async def ws_handler(self, websocket: ws.ClientConnection):
        message = await websocket.recv()
        self.logger_frame.log(message)
        if not message:
            return
        raw_data = json.dumps(message)
        msg_type = raw_data.get(ColName.TYPE.value)
        if not msg_type:
            return
        data = raw_data.get(ColName.DATA.value)
        if not data:
            return
        handler = self._chm.get_handler(msg_type)
        if not handler:
            return
        await handler.handle(websocket, data)

    async def listen(self):
        while True:
            try:
                async with ws.connect(self._uri) as websocket:
                    self._websocket = websocket
                    self.logger_frame.log(f"#{websocket.id} Connection opened.")
                    while True:
                        try:
                            await self.ws_handler(websocket)
                        except ws.ConnectionClosed:
                            self.logger_frame.log(f"#{websocket.id} Connection closed.")
                            break
            except ConnectionError:
                if self._closed:
                    break
                self.logger_frame.log("Connection failed. Retry after 5 secs.")
                await asyncio.sleep(5)

    def destroy(self):
        self._closed = True

        return super().destroy()

    def listen_thread(self):
        asyncio.run(self.listen())

    def switch_frame(self, frame: ctk.CTkFrame):
        if self.main_frame:
            self.main_frame.pack_forget()
        self.main_frame = frame
        self.main_frame.pack(expand=True, fill="both")

    def initialize(self):
        if self._debug:
            self.switch_frame(self.logger_frame)
        else:
            self.switch_frame(self.entrance_frame)

        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()


async def main():
    chm = ClientHandlerManager()

    spe_handler = handlers.SuccessPlayerEnterHandler()

    rh = handlers.ResponseHandler()
    rh.bind(Code.SUCCESS_PLAYER_ENTER, spe_handler)

    chm.bind(MsgType.RESPONSE, rh)

    root = ClientGUI(chm, debug=True, uri="ws://127.0.0.1:8001")
    root.initialize()
    root.mainloop()


if __name__ == "__main__":
    asyncio.run(main())
import base64
import logging
import json

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


class Player:
    def __init__(self, sock, addr, username, is_host):
        self.socket = sock
        self.addr = addr
        self.username = username
        self.is_readied = False
        self.is_host = is_host
        self.map = []

    def _change_map(self, game_map):
        self.map = game_map

    def change_map(self, game_map):
        self.change_map(game_map)
        self.send("mapChanged", -3, game_map=self.map)

    def send(self, _type, echo, **message):
        self._send(_type, echo, message)

    def _send(self, _type, echo, message):
        data = json.dumps({
            "type": _type, "data": message, "echo": echo})
        logger.debug(f"发送{self.addr}消息 {data}")
        self.socket.send(base64.b64encode(data.encode("utf-8")) + b"|")

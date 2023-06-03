import socket
import logging
import json
import threading
import map
import base64
import player
import uuid
import time

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
players = {}
host_client_id = str(uuid.uuid1())

# 回声范围划分
# 0~99999：客户端信息上报
# -1：聊天信息
# -2：玩家列表更新信息
# -3：地图更改
# -4：游戏开始事件


class Handler:
    def __init__(self, sock, addr, config):
        logger.info(f"{addr} 已连接到服务器")
        self.socket = sock
        self.config = config
        self.addr = addr
        self.player_id = None
        self.is_host = False
        self.server_config = json.load(open("./config.json", encoding="utf-8"))
        self.run()

    def start_game(self):
        logger.info("正在准备开始 ...")
        game_map = map.create_map()
        logger.info("地图已创建：{game_map}")
        # 在这里加密
        # 分发地图
        for player in list(players.values()):
            player._change_map(game_map)
        self.send2all("gameStarted", -4, game_map=game_map)

    def parse_recv(self, text):
        return json.loads(base64.b64decode(text))

    def login(self, username, password, client_id):
        global players
        logger.info(f"客户端{self.addr}的 Client ID 是：{client_id}")
        if password == self.config["password"]:
            if client_id == host_client_id:
                self.is_host = True
                logger.info(f"已将客户端{self.addr}设为主机")
            self.player = player.Player(
                self.socket, self.addr, username, self.is_host)
            self.player_id = self.addr[1]
            players[self.addr[1]] = self.player
            logger.info(f"客户端{self.addr}已登录：{self.player.username}")
            # 全局广播
            self.send2all(
                "newMessage", -1, msg=f"{self.player.username} has joined the game.", user_name="SYSTEM")
            self.changePlayerList()
            return True
        else:
            logger.warning(f"客户端{self.addr}登录失败：错误的密码")
            return False

    def changePlayerList(self):
        player_list = []
        for p in list(players.values()):
            player_list += [{
                "addr": list(p.addr),
                "user": p.username,
                "readied": p.is_readied,
                "host": p.is_host
            }]
        logger.info(f"玩家列表：{player_list}")
        self.send2all("playerListChanged", -2, player_list=player_list)

    def __del__(self):
        global players
        if self.player_id:
            players.pop(self.player_id)
        self.socket.close()
        self.changePlayerList()
        logger.warning(f"客户端{self.addr}已离线，对象销毁")

    def send(self, _type, echo, **message):
        self._send(_type, echo, message)

    def _send(self, _type, echo, message):
        data = json.dumps({
            "type": _type, "data": message, "echo": echo})
        logger.info(f"发送{self.addr}消息 {data}")
        self.socket.send(base64.b64encode(data.encode("utf-8")) + b"|")

    def run(self):
        while True:
            receive = self.socket.recv(
                self.server_config["receive_size"]).split(b"|")[:-1]
            for recv in receive:
                recv_data = self.parse_recv(recv)
                logger.info(f"收到{self.addr}消息 {recv_data}")
                if recv_data["type"] == "clientLogin":
                    if self.login(recv_data["data"]["username"],
                                  recv_data["data"]["password"],
                                  recv_data["data"]["client_id"]):
                        self.send(
                            "logined",
                            recv_data["echo"],
                            is_host=self.is_host)
                    else:
                        self.send("cannotLogin", recv_data["echo"], msg="密码错误")
                        del self
                        break
                elif recv_data["type"] == "getTime":
                    self.send("executed", recv_data["echo"], _time=time.time())
                elif recv_data["type"] == "changeReadyStatus":
                    self.player.is_readied = recv_data["data"]["readied"]
                    self.changePlayerList()
                elif recv_data["type"] == "startGame":
                    self.start_game()

                elif recv_data["type"] == "sendMessage":
                    self.send2all(
                        "newMessage", -1, msg=recv_data["data"]["msg"], user_name=self.player.username)

    def send2all(self, _type, echo, **message):
        logger.info(f"正在广播 {message}")
        for p in list(players.values()):
            p._send(_type, echo, message)
        logger.info(f"已对{len(list(players.values()))}个客户端广播消息")


class Server:
    def __init__(self, config):
        self.config = config
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_config = json.load(open("./config.json", encoding="utf-8"))
        logger.debug(f"服务器配置：{self.server_config}")
        self.clients = {}
        self.run()

    def run(self):
        self.socket.bind(self.config["addr"])
        self.socket.listen(self.server_config["max_connection"])
        self.server_thread = threading.Thread(target=self.loop)
        self.server_thread.start()

    def loop(self):
        logger.info("Server Started")
        while True:
            sock, addr = self.socket.accept()
            threading.Thread(
                target=lambda: Handler(
                    sock, addr, self.config)).start()


if __name__ == "__main__":
    logger.warning("请使用 main.py 启动程序")
    # 从 main.py 启动主类
    import main
    import os
    app = main.Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)

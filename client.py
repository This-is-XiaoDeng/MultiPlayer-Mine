import socket
import logging
import base64
import json
import threading
import game_window
import random
import time

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.DEBUG
)
logger = logging.getLogger(__name__)


class Client:
    def __init__(self, config, client_id):
        self.config = config
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_config = json.load(open("./config.json", encoding="utf-8"))
        logger.debug(f"客户端配置：{self.client_config}")
        self.client_id = client_id
        logger.info(f"Client ID：{client_id}")
        self.echo = 0
        self.receive = []
        # 在此处初始化PyGame
        self.run()
    
    def run(self):
        self.socket.connect(self.config["addr"])
        # self.client_thread = threading.Thread(target=self.handle)
        # self.client_thread.start()
        self.receive_thread = threading.Thread(target=self.get_receive)
        self.receive_thread.start()
    
    def get_ping(self):
        while True:
            logger.info("正在更新网络延时 ...")
            try:
                send_time = self.get_recv(self.send("getTime"))["data"]["_time"]
                self.window.update_ping(int((time.time() - send_time) * 1000))
                time.sleep(1)
            except BaseException as e:
                logger.error(e)
        
    
    def get_receive(self):
        logger.info("接收线程启动")
        while True:
            recv_data = self.socket.recv(self.client_config["receive_size"])
            recv_data = recv_data.split(b"|")
            for data in recv_data[:-1]:
                logger.debug(base64.b64decode(data))
                self.receive.append(json.loads(base64.b64decode(data)))
                logger.info(f"接收 {self.receive[-1]}")
    
    def get_recv(self, echo):
        while True:
            length = 0
            for data in self.receive:
                if data["echo"] == echo:
                    return self.receive.pop(length)
                length += 1
    
    def handle(self):
        # 用于与服务器通讯，不知道取什么名，先这样吧
        logger.info("已连接到服务器")
        self.login()        
        logger.info("正在初始化主窗口 ...")
        self.window = game_window.Window(self)
        # 延迟获取线程
        self.get_ping_thread = threading.Thread(target=self.get_ping)
        self.get_ping_thread.start()
        # 进入循环
        self.window.loop()
        logger.warning("主窗口已退出")
        
        
    
    def login(self):
        logger.info("正在登录 ...")
        login_res = self.get_recv(
            self.send(
                "clientLogin",
                username=self.config["username"],
                password = self.config["password"],
                client_id=self.client_id))
        if login_res["type"] == "logined":
            logger.info("登录成功")
            self.is_host = login_res["data"]["is_host"]
            return True
        else:
            return False
        
    def send(self, _type, **message):
        echo = random.randint(0, 99999)
        data = json.dumps({
            "type": _type, "data": message, "echo": echo})
        logger.info(f"发送 {data}")
        self.socket.send(base64.b64encode(data.encode("utf-8")) + b"|")
        # self.echo += 1
        return echo
        
        
if __name__ == "__main__":
    logger.warning("请使用 main.py 启动程序")
    # 从 main.py 启动主类
    import main, os
    app = main.Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)
    
import sys
import logging
import server
import join
import os
import client
import time

logging.basicConfig(
    format="[%(asctime)s][%(name)s \\ %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
client_id = server.host_client_id


class Main:
    def __init__(self):
        logger.info("mine_multiplayer v1.0.0")
        self.get_config()
        self.run()

    def run(self):
        if self.config["type"]:
            self.start_server()
        self.client = client.Client(self.config, client_id)
        self.client.handle()
        logger.warning("客户端已退出")

    def start_server(self):
        self.server = server.Server(self.config)

    def get_config(self):
        self.config = join.show()
        logger.info("加入窗口关闭")
        logger.debug(self.config)


if __name__ == "__main__":
    app = Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)

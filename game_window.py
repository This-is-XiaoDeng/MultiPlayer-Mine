import pygame
import time
import logging
import threading
import draw
import easygui

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.DEBUG
)
logger = logging.getLogger(__name__)


class Window:
    def __init__(self, client):
        self.timer_launch = time.time()
        logger.info(f"PyGame已初始化：{pygame.init()}")
        # 初始化变量
        self.screen = "ready"
        self.is_running = True
        self.client = client
        self.is_host = self.client.is_host
        self.mouse_pos = (0, 0)
        self.fps = 0
        self._fps = 0
        self.mouse_clicked = False
        self.is_readied = False
        # self.send_chat_msg_thread = threading.Thread(target=self.send_chat_message)
        self.ping = 0
        self.player_list = self.client.get_recv(-2)["data"]["player_list"]
        self.timer_fps = 0
        self.config = self.client.config
        self.can_start = False
        self.messages = []
        self.font = "sarasa-fixed-cl-regular.ttf"
        self.bg_color = (45,64,89)#(50,62,79)#(30,31,41)
        self.get_message_thread = threading.Thread(target=self.get_message)
        # 初始化素材
        self.debug_display_font = pygame.font.Font(self.font, 10)
        self.ready_title = pygame.font.Font(self.font, 50).render(
            "GETTING READY", True, (255,255,255))
        self.player_list_display_font = pygame.font.Font(self.font, 15)
        self.chat_display_font = pygame.font.Font(self.font, 12)
        # 初始化窗口
        self.window = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Multiplayer Mine v1.0.0-dev (By This-is-XiaoDeng)")
        self.get_message_thread.start()
        threading.Thread(target=self.start_game).start()
    
    def start_game(self):
        logger.info("游戏开始事件监控线程已启动！")
        while True:
            recv_data = self.client.get_recv(-4)
            if recv_data["type"] == "gameStarted":
                self.map = recv_data["data"]["game_map"]
                # TODO 启动地图更新和排名更新线程
                self.screen = "pvp"
                logger.info("游戏开始")
    
    def get_message(self):
        while True:
            msg = self.client.get_recv(-1)
            logger.info(f"[CHAT] {msg['data']['user_name']}: {msg['data']['msg']}")
            self.messages.append(msg['data'])
            
    
    def update_palyer_list(self):
        while self.screen == "ready":
            self.player_list = self.client.get_recv(-2)["data"]["player_list"]
            _can_start = True
            if self.is_host:
                for player in self.player_list:
                    if not player["readied"]:
                        _can_start = False
                self.can_start = _can_start
        
    def update_ping(self, ping):
        logger.info(f"网络延迟：{ping}ms")
        self.ping = ping
    
    def display_debug_info(self):
        """self.window.blit(
            self.debug_display_font.render(f"", True, (255, 255, 255)),
            (0, 0))"""
        surface =  self.debug_display_font.render(
            (
                "Multiplayer Mine v1.0.0-dev |"
                 f" FPS: {self.fps} | PING: {self.ping}ms |"
                 f" {self.config['addr'][0]}:{self.config['addr'][1]}"
            ), True, (240,240,240))
        surface.set_alpha(85)
        self.window.blit(surface, ((600 - surface.get_size()[0])/2, 385))
        # 计算fps
        if time.time() - self.timer_fps >= 1:
            self.timer_fps = time.time()
            self.fps = self._fps
            self._fps = 0
        else:
            self._fps += 1
        
    def display_ready_screen(self):
        self.window.blit(self.ready_title, ((600-self.ready_title.get_size()[0])/2, 30))
        # 玩家列表
        player_list_surface = pygame.surface.Surface((500, 150))
        player_list_surface.fill((30,31,41))
        length = 0
        for player in self.player_list:
            length += 1
            player_list_surface.blit(
                self.player_list_display_font.render(
                    f'{length}. {player["user"]}{" [HOST]" if player["host"] else ""}{" (READIED)" if player["readied"] else ""}',
                    True, (255, 255, 255)),
                (5, 20 * length - 15)
            )
        self.window.blit(player_list_surface, (50, 100))
        # 准备按钮
        ready_btn = pygame.surface.Surface((375, 60))
        if self.can_start:
            ready_btn.fill((0,128,143))
            text = self.player_list_display_font.render("START", True, (255, 255, 255))
        else:
            ready_btn.fill((30,31,41))
            text = self.player_list_display_font.render(
                "READIED" if self.is_readied else "READY", True, (255, 255, 255))
        size = text.get_size()
        ready_btn.blit(text, ((375-size[0])/2,(60-size[1])/2))
        self.window.blit(ready_btn, (50, 270))
        # 查看设置按钮
        setting_btn = pygame.surface.Surface((100, 60))
        setting_btn.fill((30,31,41))
        text =self.player_list_display_font.render("SETTING", True, (255, 255, 255))
        size = text.get_size()
        setting_btn.blit(text, ((100-size[0])/2,(60-size[1])/2))
        self.window.blit(setting_btn, (450, 270))
        # 处理事件
        if self.mouse_clicked and 50 <= self.mouse_pos[0] <= 425 and 270 <= self.mouse_pos[1] <= 330:
            logger.info("点击按钮：准备/取消准备/开始")
            if self.can_start:
                self.client.send("startGame")
            else:
                self.is_readied = not self.is_readied
                self.client.send("changeReadyStatus", readied = self.is_readied)
                
        elif self.mouse_clicked and 450 <= self.mouse_pos[0] <= 550 and 270 <= self.mouse_pos[1] <= 330:
            logger.info("点击按钮：修改/查看设置")
            if self.is_host:
                self.client.send(
                    "changeGameSettings",
                    settings=easygui.multenterbox("修改游戏设置", "设置", ["长", "宽", "数量"], ["9", "9", "10"]))
        # 渲染聊天信息
        length = 0
        for msg in self.messages[-3:][::-1]:
            length += 1
            text = self.chat_display_font.render(f"{msg['user_name']}: {msg['msg']}", True, (255, 255, 255))
            self.window.blit(text, (0, 385 - length * 15))
        text = self.chat_display_font.render(f"PRESS [T] TO INPUT", True, (166, 166, 166))
        self.window.blit(text, (0, 385))
    
    def send_chat_message(self):
        logger.info("正在获取发送信息 ...")
        msg = easygui.enterbox("请输入消息内容", "发送消息")
        logger.debug(msg)
        self.client.send("sendMessage", msg=msg)
    
    def display_pvp_ui(self):
        map_surface = draw.draw(self.map)
        self.window.blit(map_surface, ((300 - map_surface.get_size()[0]) / 2,
                                (400 - map_surface.get_size()[1]) / 2))
        
    def loop(self):
        self.update_player_list_thread = threading.Thread(target=self.update_palyer_list)
        self.update_player_list_thread.start()
        logger.info(f"客户端加载完成！（用时{round(time.time() - self.timer_launch, 3)}s）")
        while self.is_running:
            # 处理事件
            for event in pygame.event.get():
                logger.debug(f"[EVENT] {event}")
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        #threading.Thread(
                            #target=self.send_chat_message).start()
                            #self.send_chat_msg_thread.start()
                        self.send_chat_message()
                        
            # 处理screen
            if self.screen == "ready":
                self.display_ready_screen()
            elif self.screen == "pvp":
                self.display_pvp_ui()
            # 处理Debug事件
            self.display_debug_info()
            # 更新屏幕
            pygame.display.update()
            self.window.fill(self.bg_color)
            pygame.time.delay(int(1/self.client.client_config["max_fps"]*1000))
            self.mouse_clicked = False
            # 检查线程
            if not self.client.get_ping_thread.is_alive():
                self.client.get_ping_thread = threading.Thread(target=self.client.get_ping)
                self.client.get_ping_thread.start()
            

if __name__ == "__main__":
    logger.warning("请使用 main.py 启动程序")
    # 从 main.py 启动主类
    import main, os
    app = main.Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)
        

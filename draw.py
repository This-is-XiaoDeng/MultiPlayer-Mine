import pygame
import logging


logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
pygame.init()

font = pygame.font.Font("sarasa-fixed-cl-regular.ttf", 18)
timer_font = pygame.font.Font("sarasa-fixed-cl-regular.ttf", 46)
BLOCK_SIZE = 210 / 9
_map = None
_surface = None


def draw_map(game_map, selected=None):
    global _map, _surface
    if game_map != _map:
        logger.info("开始绘制地图 ...")
        # 初始化
        surface = pygame.surface.Surface(
            (len(game_map) * BLOCK_SIZE, len(game_map[0]) * BLOCK_SIZE))  # (210, 210))
        width, height = 7.5, 7.5
        surface.fill((0, 255, 0))
        surface.set_colorkey((0, 255, 0))
        # 开始绘制
        for row in game_map:
            logger.info(f"已选定行：{row}")
            for column in row:
                if column >= 0:
                    pygame.draw.rect(
                        surface, (255, 255, 255), (width, height, 18, 18))
                elif -9 <= column < 0:
                    text = font.render(str(-column), True, (255, 255, 255))
                    pos = (
                        width + (18 - text.get_size()[0]) / 2,
                        height + (18 - text.get_size()[1]) / 2)
                    surface.blit(text, pos)
                logger.info(f"已绘制 {column} 于 {(width, height)}")
                width += 22.5
            width = 7.5
            height += 22.5
        # 写入缓存
        _map = game_map
        _surface = surface
        # 返回数据
        return surface
    else:
        # 检测到缓存，跳过渲染
        surface = _surface.copy()
        if selected:
            pygame.draw.rect(
                surface,
                (187,
                 187,
                 187),
                (22.5 *
                 selected[0] +
                    7.5,
                    22.5 *
                    selected[1] +
                    7.5,
                    18,
                    18))
        return surface


def draw(game_map, selected=None):
    map_size = (len(game_map), len(game_map))
    surface_size = (
        map_size[0] *
        BLOCK_SIZE +
        20,
        map_size[1] *
        BLOCK_SIZE +
        100)
    surface = pygame.surface.Surface(surface_size)
    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, (0, 0, 0),
                     (5, 5, surface_size[0] - 10, surface_size[1] - 10))
    surface.set_colorkey((0, 0, 0))
    map_surface = draw_map(game_map, selected)
    map_pos = (10, surface_size[1] - map_surface.get_size()[1] - 10)
    surface.blit(map_surface, map_pos)

    surface.blit(timer_font.render("000", True, (255, 255, 255)), (20, 25))
    finished = timer_font.render("000", True, (255, 255, 255))
    surface.blit(finished, (surface_size[0] - 20 - finished.get_size()[0], 25))

    return surface, map_pos, map_surface.get_size()


if __name__ == "__main__":
    logger.warning("请使用 main.py 启动程序")
    # 从 main.py 启动主类
    import main
    import os
    app = main.Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)

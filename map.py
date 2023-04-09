import random
import logging

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.DEBUG
)
logger = logging.getLogger(__name__)
NULL = 0
BOMB = 9


def create_map(width = 9, height = 9, count = 10):
    mine_map = []
    for i1 in range(width):
        mine_map.append([])
        for _ in range(height):
            mine_map[i1].append(NULL)
    for i in range(count):
        while True:
            pos = (random.randint(0, width - 1), random.randint(0, width - 1))
            if not mine_map[pos[0]][pos[1]]:
                mine_map[pos[0]][pos[1]] = BOMB #"bomb"
                break
    row_count = 0
    for row in mine_map:
        column_count = 0
        for column in row:
            if not column:
                bomb_count = 0
                if row_count != 0:
                    for item in mine_map[row_count - 1][max(column_count - 1, 0):column_count + 2]:
                        if item == BOMB:
                            bomb_count += 1
                if row_count != width - 1:
                    for item in mine_map[row_count + 1][max(column_count - 1, 0):column_count + 2]:
                        if item == BOMB:
                            bomb_count += 1
                for item in row[max(column_count - 1, 0):column_count + 2]:
                    if item == BOMB:
                        bomb_count += 1
                if bomb_count:
                    mine_map[row_count][column_count] = bomb_count
            column_count += 1
        row_count += 1
    # DEBUG
    # END: DEBUG
    return mine_map
        

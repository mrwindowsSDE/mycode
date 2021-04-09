import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
GLOBAL_GAME_MAPS = {}


def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))


def frontend_user_turn(game_map, row, column):
    is_valid_location(game_map, row, column)
    if game_map.get("valid_location"):
        drop_piece(game_map, row, column)


def is_valid_location(game_map, row, column):
    if game_map.get("board")[row][column] == 0:
        game_map["valid_location"] = True
    else:
        game_map["valid_location"] = False
    return game_map


def drop_piece(game_map, row, column):
    game_map.get("board")[row][column] = game_map.get("turn")
    print(game_map.get("board"))
    return game_map


def end_round(game_map):
    turn = game_map.get("turn")
    if turn == 1.0:
        game_map["turn"] = 2.0
    else:
        game_map["turn"] = 1.0
    return game_map

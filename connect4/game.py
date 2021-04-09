import numpy as np
import view
from pipeop import pipes
from win_determiner import win_determiner
import sys

VALID_SELECTIONS = ["0", "1", "2", "3", "4", "5", "6"]
ROW_COUNT = 6
COLUMN_COUNT = 7


def start(game_map):
    board = create_board()
    game_map["board"] = board
    round_map = game_map
    while True:
        round_map = play(round_map)


@pipes
def play(game_map):
    return (
        game_map
        >> user_turn
        >> get_next_valid_row
        >> drop_piece
        >> win_determiner(
            [game_map.get("next_valid_row"), int(game_map.get("selection"))]
        )
        >> end_round
        >> debug
    )


def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))


def user_turn(game_map):
    selection = ""
    while selection not in VALID_SELECTIONS:
        selection = input(view.user_selection_text(game_map.get("turn")))
    game_map["selection"] = int(selection)
    is_valid_location(game_map)
    if not game_map.get("valid_location"):
        user_turn(game_map)
    else:
        return game_map


def is_valid_location(game_map):
    selection = game_map.get("selection")
    if game_map.get("board")[ROW_COUNT - 1][selection] == 0:
        game_map["valid_location"] = True
    return game_map


def get_next_valid_row(game_map):
    selection = game_map.get("selection")
    for r in range(ROW_COUNT):
        if game_map.get("board")[r][selection] == 0:
            game_map["next_valid_row"] = r
    return game_map


def drop_piece(game_map):
    row = game_map.get("next_valid_row")
    selection = game_map.get("selection")
    piece = game_map.get("turn")
    game_map.get("board")[row][selection] = piece
    return game_map


def end_round(game_map):
    if game_map.get("final_result"):
        sys.exit(f"Player {game_map.get('turn')} won!")
    else:
        turn = game_map.get("turn")
        if turn == 1.0:
            game_map["turn"] = 2.0
        else:
            game_map["turn"] = 1.0
    return game_map


def debug(game_map):
    print(game_map)
    return game_map


def main():
    start({"turn": 1.0})


if __name__ == "__main__":
    main()

#!/usr/bin/python3
from flask import Flask, jsonify
from flask_limiter.util import get_remote_address
from frontend_win_determiner import win_determiner
from frontend_game import (
    GLOBAL_GAME_MAPS,
    create_board,
    frontend_user_turn,
    end_round,
)
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@cross_origin()
@app.route("/placepiece/<int:row>/<int:column>")
def place_piece(row, column):
    game_map = get_game_map()
    data_to_return = {}
    frontend_user_turn(game_map, row, column)
    if game_map.get("valid_location"):
        win_determiner(game_map, game_map.get("turn"))
        end_round(game_map)
        if game_map.get("final_result"):
            clear_board()
            data_to_return = jsonify({"ok": True, "won": True})
        else:
            data_to_return = jsonify({"ok": True, "won": False})
    else:
        data_to_return = jsonify({"ok": False, "won": False})
    return data_to_return


def get_game_map():
    if not GLOBAL_GAME_MAPS.get(get_remote_address):
        board = create_board()
        GLOBAL_GAME_MAPS[get_remote_address] = {"turn": 1.0, "board": board}
    return GLOBAL_GAME_MAPS.get(get_remote_address)


def clear_board():
    GLOBAL_GAME_MAPS[get_remote_address].clear()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2226)

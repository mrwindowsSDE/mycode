from pipeop import pipes


@pipes
def win_determiner(game_map, board_start):
    game_map["start"] = board_start
    game_map["results"] = []
    return (
        game_map
        >> check_win_down
        >> check_win_left
        >> check_win_right
        >> check_win_left_diag_up
        >> check_win_right_diag_up
        >> check_win_left_diag_down
        >> check_win_right_diag_down
        >> determine_result
    )


def check_win_down(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    row = start[0]
    item = start[1]
    total = 1
    try:
        for x in range(1, 4):
            if board[row + x][item] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_left(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    item = start[1]
    row = start[0]
    total = 1
    try:
        for x in range(1, 4):
            if board[row][item - x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_right(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    item = start[1]
    row = start[0]
    total = 1
    try:
        for x in range(1, 4):
            if board[row][item + x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_right_diag_down(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    row = start[0]
    item = start[1]
    total = 1
    try:
        for x in range(1, 4):
            if board[row + x][item + x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_left_diag_down(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    row = start[0]
    item = start[1]
    total = 1
    try:
        for x in range(1, 4):
            if board[row + x][item - x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_right_diag_up(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    row = start[0]
    item = start[1]
    total = 1
    try:
        for x in range(1, 4):
            if board[row - x][item + x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def check_win_left_diag_up(game_map):
    start = game_map.get("start")
    player = game_map.get("turn")
    board = game_map.get("board")
    row = start[0]
    item = start[1]
    total = 1
    try:
        for x in range(1, 4):
            if board[row - x][item - x] == player:
                total += 1
            else:
                break
        if total == 4:
            game_map["results"].append(True)
    except IndexError:
        pass
    return game_map


def determine_result(game_map):
    results = game_map.get("results")
    if True in results:
        game_map["final_result"] = True
    else:
        game_map["final_result"] = False
    return game_map

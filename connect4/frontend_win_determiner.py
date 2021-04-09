def win_determiner(game_map, player):
    board = game_map.get("board")
    player = game_map.get("turn")
    column_count = 7
    row_count = 6
    for column in range(column_count - 3):
        for row in range(row_count):
            if (
                board[row][column] == player
                and board[row][column + 1] == player
                and board[row][column + 2] == player
                and board[row][column + 3] == player
            ):
                game_map["final_result"] = True

    for column in range(column_count):
        for row in range(row_count - 3):
            if (
                board[row][column] == player
                and board[row + 1][column] == player
                and board[row + 2][column] == player
                and board[row + 3][column] == player
            ):
                game_map["final_result"] = True

    for column in range(column_count - 3):
        for row in range(row_count - 3):
            if (
                board[row][column] == player
                and board[row + 1][column + 1] == player
                and board[row + 2][column + 2] == player
                and board[row + 3][column + 3] == player
            ):
                game_map["final_result"] = True

    for column in range(column_count - 3):
        for row in range(3, row_count):
            if (
                board[row][column] == player
                and board[row - 1][column + 1] == player
                and board[row - 2][column + 2] == player
                and board[row - 3][column + 3] == player
            ):
                game_map["final_result"] = True
    return game_map

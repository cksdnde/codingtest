def solution(keyinput, board):
    position = [0, 0]

    max_x = (board[0] - 1) // 2
    max_y = (board[1] - 1) // 2

    for key in keyinput:
        if key == "up":
            position[1] += 1
        elif key == "down":
            position[1] -= 1
        elif key == "left":
            position[0] -= 1
        elif key == "right":
            position[0] += 1

        position[0] = max(-max_x, min(max_x, position[0]))
        position[1] = max(-max_y, min(max_y, position[1]))

    return position
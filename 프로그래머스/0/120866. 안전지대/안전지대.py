def solution(board):
    rows = len(board)
    cols = len(board[0])

    danger_zone = [[0] * cols for _ in range(rows)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                danger_zone[r][c] = 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        danger_zone[nr][nc] = 1

    safe_count = 0
    for r in range(rows):
        for c in range(cols):
            if danger_zone[r][c] == 0:
                safe_count += 1
    
    return safe_count
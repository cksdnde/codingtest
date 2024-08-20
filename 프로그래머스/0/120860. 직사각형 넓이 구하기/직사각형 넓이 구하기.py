def solution(dots):
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    x1, x2 = set(x_coords)
    y1, y2 = set(y_coords)
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return width * height
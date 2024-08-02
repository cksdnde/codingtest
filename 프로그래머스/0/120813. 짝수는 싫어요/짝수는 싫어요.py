def solution(n):
    numbers = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            numbers.append(i)
    return numbers
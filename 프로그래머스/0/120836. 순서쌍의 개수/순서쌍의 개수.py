import math

def solution(n):
    count = 0
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            b = n // a
            if a == b:
                count += 1
            else:
                count += 2
    return count
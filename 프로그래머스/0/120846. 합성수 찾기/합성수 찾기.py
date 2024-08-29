def solution(n):
    def is_composite(x):
        count = 0
        for i in range(1, x+1):
            if x % i == 0:
                count += 1
        return count >= 3

    composite_count = 0
    for i in range(1, n + 1):
        if is_composite(i):
            composite_count += 1
            
    return composite_count
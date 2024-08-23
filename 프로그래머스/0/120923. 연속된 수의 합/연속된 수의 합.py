def solution(num, total):

    start = (total - (num * (num - 1)) // 2) // num

    result = [start + i for i in range(num)]

    return sorted(result)
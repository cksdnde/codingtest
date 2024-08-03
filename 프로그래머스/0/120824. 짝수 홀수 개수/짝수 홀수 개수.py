def solution(list):
    count = sum(1 for num in list if num % 2 == 0)
    count1 = len(list) - count
    return [count, count1]
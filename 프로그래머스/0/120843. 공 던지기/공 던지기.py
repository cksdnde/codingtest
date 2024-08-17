def solution(numbers, k):

    index = (k * 2 - 2) % len(numbers)
    return numbers[index]

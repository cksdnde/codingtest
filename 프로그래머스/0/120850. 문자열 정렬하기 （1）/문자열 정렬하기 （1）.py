def solution(my_string):
    digits = [int(char) for char in my_string if char.isdigit()]
    digits.sort()
    return digits
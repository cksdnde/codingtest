import re

def solution(my_string):

    numbers = re.findall(r'\d+', my_string)

    total_sum = sum(map(int, numbers))
    
    return total_sum
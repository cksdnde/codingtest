def solution(array, n):
    closest_num = array[0]
    min_diff = abs(array[0] - n)
    for num in array:
        diff = abs(num - n)
        if diff < min_diff or (diff == min_diff and num < closest_num):
            closest_num = num
            min_diff = diff
    
    return closest_num

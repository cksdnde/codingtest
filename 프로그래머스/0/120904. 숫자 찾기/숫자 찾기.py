def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    position = num_str.find(k_str)
    
    if position != -1:
        return position + 1
    else:
        return -1
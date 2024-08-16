def solution(s):
    elements = s.split()
    total = 0
    last_number = 0
    
    for elem in elements:
        if elem == "Z":
            total -= last_number
        else:
            last_number = int(elem)
            total += last_number
    return total
def solution(box, n):
    length_fit = box[0] // n
    width_fit = box[1] // n
    height_fit = box[2] // n
    
    return length_fit * width_fit * height_fit
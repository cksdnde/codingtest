def solution(array):
    answer = []
    max_value = max(array)
    answer.append(max_value)
    i= 0
    for i in range(len(array)):
        if max_value == array[i]:
            answer.append(i)
        i+=1
    return answer
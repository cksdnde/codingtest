def solution(n):
    answer = 0
    line = list(map(int,str(n)))
    for i in range(0,len(line)):
        answer += line[i]
    return answer
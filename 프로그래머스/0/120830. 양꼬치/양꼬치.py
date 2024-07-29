def solution(num1, num2):
    cost = num1 * 12000
    fdrinks = num1 // 10
    pdrinks = max(0, num2 - fdrinks) 
    dcost = pdrinks * 2000
    result = cost + dcost
    return result
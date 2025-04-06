import math

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 합을 구하기
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    
    # 최대공약수(GCD)로 나누기
    gcd = math.gcd(numerator, denominator)
    
    # 기약분수로 만들기
    numerator //= gcd
    denominator //= gcd
    
    return [numerator, denominator]

# 예시 입력
print(solution(1, 2, 3, 4))  # 출력: [5, 4]
print(solution(9, 2, 1, 3))  # 출력: [29, 6]

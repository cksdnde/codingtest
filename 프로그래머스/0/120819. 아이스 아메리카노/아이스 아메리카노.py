def solution(money):
    price = money//5500
    lprice = money % 5500
    return [price,lprice]
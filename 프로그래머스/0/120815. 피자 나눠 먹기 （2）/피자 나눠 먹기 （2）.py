def solution(n):

    pizzas = 1

    while (pizzas * 6) % n != 0:
        pizzas += 1
    
    return pizzas
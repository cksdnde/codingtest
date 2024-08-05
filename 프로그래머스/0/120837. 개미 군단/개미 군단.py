def solution(hp):
    ant1 = hp//5
    hp_ant1 = hp%5
    
    ant2 = hp_ant1//3
    hp_ant2 = hp_ant1%3
    
    ant3 = hp_ant2//1
    return ant1+ant2+ant3
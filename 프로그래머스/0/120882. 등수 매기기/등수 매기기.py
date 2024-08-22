def solution(score):
    averages = [(s[0] + s[1]) / 2 for s in score]

    sorted_averages = sorted(averages, reverse=True)
    ranks = [sorted_averages.index(avg) + 1 for avg in averages]
    
    return ranks
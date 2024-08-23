def solution(array):
    from collections import Counter

    counter = Counter(array)

    most_common = counter.most_common()

    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]
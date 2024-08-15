def solution(s):
    from collections import Counter
    char_count = Counter(s)
    single_occurrence_chars = [char for char in char_count if char_count[char] == 1]
    single_occurrence_chars.sort()
    return ''.join(single_occurrence_chars)

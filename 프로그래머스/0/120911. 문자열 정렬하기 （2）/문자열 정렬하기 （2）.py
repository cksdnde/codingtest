def solution(my_string):
    lowercased_string = my_string.lower()

    sorted_string = ''.join(sorted(lowercased_string))

    return sorted_string
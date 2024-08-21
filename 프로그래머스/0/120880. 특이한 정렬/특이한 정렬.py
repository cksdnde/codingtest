def solution(n, numlist):

    if isinstance(n, list) and isinstance(numlist, int):

        n, numlist = numlist, n

    if not isinstance(numlist, list):
        print(f"Invalid input: numlist is {type(numlist).__name__}, expected a list.")
        return []

    try:
        sorted_list = sorted(numlist, key=lambda x: (abs(x - n), -x))
        return sorted_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
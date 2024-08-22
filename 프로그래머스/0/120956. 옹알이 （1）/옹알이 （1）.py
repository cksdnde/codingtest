def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        temp_word = word
        for sound in valid_sounds:
            temp_word = temp_word.replace(sound, ' ')
        if temp_word.strip() == '':
            count += 1
    
    return count
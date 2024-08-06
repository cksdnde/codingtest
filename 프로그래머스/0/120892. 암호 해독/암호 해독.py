def solution(cipher, code):
    decrypted_message = ''
    for i in range(code - 1, len(cipher), code):
        decrypted_message += cipher[i]
    return decrypted_message
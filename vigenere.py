from typing import *

alphabet_length = 26


def encrypt(data :str, keyword :str, do_decrypt :bool = False):
    factor :int = -1 if do_decrypt else 1
    encrypted :str = ''
    for i in range(len(data)):
        new_char :str = chr( ((ord(data[i]) - ord('A') + factor * ord(keyword[i % len(keyword)]) - ord('A')) % alphabet_length)  + ord('A'))
        encrypted += new_char
    return encrypted


if __name__ == '__main__':

    plaintext = "GCYCZFMLYLEIM"
    keyword = "AYUSH"

    encrypted = encrypt(plaintext, keyword, True)
    print(encrypted)
    pass

# GCYCZFMLYLEIM
# GEEKSFORGEEKS
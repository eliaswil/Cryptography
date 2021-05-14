from typing import *
import math



def extract_lines(plaintext :str, key :int):
    lines = [''] * key
    current_position = 0
    positions = [i for i in range(key)] + [i for i in range(key-2, 0, -1)]
    for i in range(len(plaintext)):
        lines[positions[current_position]] += plaintext[i]
        current_position = (current_position + 1) % len(positions)
    return lines



def encrypt(plaintext :str, key :int, doPrint :bool = False):
    lines = extract_lines(plaintext, key)

    if doPrint:
        print(get_zic_zac(lines, key))


    return ''.join(lines)



# region <decrypt>

def decrypt(cipher, key):
    line_lengths = [len(l) for l in extract_lines(cipher, key)] # get lines (zic-zac) for encrypted cipher -> to get the length of each line

    # build lines
    lines = []
    start = 0
    end = 0
    for l in line_lengths:
        end = start + l
        lines.append(cipher[start : end])
        start += l

    # go through the lines and get first character of each one until finished
    decrypted = ''
    indices = [i for i in range(key)] + [i for i in range(key-2, 0, -1)] # the indices for traversal - e.g.: key=4 -> [0,1,2,3,2,1]
    index = 0
    while len(lines[indices[index]]) > 0:
        decrypted += lines[indices[index]][0] # add first char to decrypted-message
        lines[indices[index]] = lines[indices[index]][1:] # delete first char from lines
        index = (index + 1) % len(indices) # change index

    return decrypted


def decrypt_brute_force(message :str, lower_limit=2, upper_limit=10):
    lower_limit = max(2, lower_limit)
    upper_limit = min(upper_limit, len(message))
    return [''.join(decrypt(message, key)) for key in range(lower_limit, upper_limit)]


# endregion


# region <print>

def get_outer_interval(key :int):
    return 2 * (key - 1) - 1

def get_zic_zac_message(message :str, key: int, spacing=' '):
    lines = extract_lines(message, key)
    return get_zic_zac(lines, key, spacing)

def get_zic_zac(lines :[str], key :int, spacing=' '):
    outer_interval = get_outer_interval(key) # space between two peaks

    space = spacing * outer_interval # total padding for the first and the last line
    left_padding = ''

    output = ''

    # first line
    output += space.join(lines[0]) + '\n'

    # middle lines
    current_interval = outer_interval
    for i in range(1, len(lines)-1):
        left_padding = spacing * i
        current_interval = current_interval - 2 # interval decreases by 2 per line
        
        output += left_padding

        index = 0

        # for each character (in a line)
        for j in range(len(lines[i])):
            paddings = [current_interval, outer_interval - 1 - current_interval] # alternating padding: key=6 -> outer_padding=9, line 1: paddings = [7, 1], line 2: paddings = [5, 3]
            output += lines[i][j] + paddings[index] * spacing # add char + padding to output
            index = (index + 1) % len(paddings) # alter padding

        output += '\n'

    # last line
    space = spacing * outer_interval
    output += spacing * (key-1) + space.join(lines[-1]) + '\n'

    return output


# endregion




if __name__ == '__main__':

    message = 'DasIstEinGanzEinLangerGartenzaun'
    encrypted = encrypt(message, 3, doPrint=True)
    print(encrypted)

    print('\n' + '-'*35 + '\n')

    decrypted = decrypt(encrypted, 3)
    print(decrypted)

    decrypted_messages = decrypt_brute_force(encrypted, 0, 10)
    print(decrypted_messages)


# 4:
# DTEBAISEGHEOHFEIIEEMTCTSNIS
# DTEBA
# ISEGHEOHF
# EIIEEMTCT
# SNIS


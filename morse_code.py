from typing import *

MORSE_CODE_DICT :Dict[str, str] = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message :str):
    return ' '.join([MORSE_CODE_DICT[c.upper()] for c in message])

def decrypt(encrypted_message :str):
    message += ' '
  
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
  
            # counter to keep track of space
            i = 0
            citext += letter

        else:
            i += 1
  
            # if i = 2 that indicates a new word
            if i == 2 :
                decipher += ' '
            else:
  
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher


if __name__ == '__main__':
    message = input('Message -> Morse: ')
    encrypted = encrypt(message)
    print(encrypted)
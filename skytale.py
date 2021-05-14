from typing import *


def encrypt(message :str, key :int):
    pass

def decrypt(encrypted_message :str, key :int):
    message = [''] * key
    position = 0
    for i in range(len(encrypted_message)):
        message[position] += encrypted_message[i]
        position = (position + 1) % key
    return ''.join(message)

def decrypt_brute_force(message :str):
    return [''.join(decrypt(message, key)) for key in range(2, 10)]

if __name__ == '__main__':
    print('Skytale -> plaintext')

    encrypted = input('- Encrypted Skytale message: ')
    decrypted = '\n\t'.join(decrypt_brute_force(encrypted))

    print('- Decrypted: ')
    print('\t' + decrypted)

# AGCNOCDHCMHIHHMTEOEEUEENNNIRK -> ACHTUNGDIEEICHHOERNCHENKOMMEN
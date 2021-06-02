from typing import *


# https://qvault.io/cryptography/how-sha-2-works-step-by-step-sha-256/

# Round Constants:
# ----------------
# can also be calculated: 
# = Each value (0-63) is the first 32 bits of the fractional parts of the cube roots of the 
#   first 64 primes (2 – 311)

K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

# hash values (hard-coded constants)
# ----------------------------------
# can also be calculated: = bits of the fractional parts of the square roots of the 
#   first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19

H = [
    0x6a09e667,
    0xbb67ae85,
    0x3c6ef372,
    0xa54ff53a,
    0x510e527f,
    0x9b05688c,
    0x1f83d9ab,
    0x5be0cd19]


block_size = 512

def rigth_rotate(number :int, rotations :int, length :int ):
    return (number >> rotations) | ((number << (length - rotations)) & ((1 << length)-1))

def left_rotate(number :int, rotations :int, length :int):
    return ((number << rotations) | (number >> (length - rotations))) & ((1 << length)-1)

def sha256(message :str):

    # convert to binary
    binary_message :int = ''.join([format(ord(c), '08b') for c in message])

    # padding

    # append a single '1'
    binary_message_padded :str = binary_message + '1'

    # fill up last 'chunk' (block) of 512 with '0's
    binary_message_padded += '0' * (block_size - len(binary_message_padded) % block_size)

    # add the lengh of the original binary intput
    binary_0 :int = int(binary_message_padded, 2) + len(binary_message)
    
    # convert to binary
    binary_0_string :str = format(binary_0, '0b')

    # if original binary message has leading 0s -> add zeros until it is a multiple of 512
    if len(binary_0_string) % block_size > 0:
        number_of_missing_zeros :int = block_size - (len(binary_0_string) % block_size)
        binary_0_string = ('0' * number_of_missing_zeros) + binary_0_string

    
    # the chunk loop

    # for each 512-bit 'chunk' of data
    for chung_start_index in range(0, len(binary_0_string), block_size):
        
        # create 32-bit-words
        _32_bit_words :List[str] = [binary_0_string[word_start_index : word_start_index + 32] for word_start_index in range(chung_start_index, block_size, 32)]
        
        # add 32-bit-words of '0's until there are 64 32-bit-words in total
        _32_bit_words += ['0' * 32] * (64 - len(_32_bit_words))

        # basically magic
        for word_index in range(len(_32_bit_words)):
            word :int = int(_32_bit_words[word_index], 2) # convert to a number
            s0 = () # TODO




    return 'TODO'

if __name__ == "__main__":
    message = 'hello world'
    hashed_message = sha256(message)
    print('\n\nhashed_message: ', hashed_message)
from typing import *

lower_case_alphabet = [chr(c) for c in range(ord('a'), ord('z')+1)]
upper_case_alphabet = [chr(c) for c in range(ord('A'), ord('Z')+1)]

def shift(message :str, shifts :int):
    new_message = ''
    for c in message:

        # lower-case
        if ord('a') <= ord(c) <= ord('z'):
            new_message += lower_case_alphabet[(ord(c) - ord('a') + shifts) % len(lower_case_alphabet)]

        # upper-case
        elif ord('A') <= ord(c) <= ord('Z'):
            new_message += upper_case_alphabet[(ord(c) - ord('A') + shifts) % len(upper_case_alphabet)]
        
        # other
        else:
            new_message += c

    return new_message

def brute_force(message):
    return [shift(message, s) for s in range(1, ord('A'))]





if __name__ == "__main__":
    print(shift('asdf', 3))

# Znuyk cnu igt osgmotk gteznotm, igt ixkgzk znk osvuyyohrk
# Those who can imagine anything, can create the impossible

    print(''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]))
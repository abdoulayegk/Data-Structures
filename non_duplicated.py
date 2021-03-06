"""Given an array of integers where every integer occurs tree times except for
one integer, which only occurs once, find and return non-duplicated integer"""

WORD_SIZE = 32
"""This question involves bit manipulations and we have the word_size of 32
bits so we perform left shift using << operand in python"""


def get_non_duplicated_number(arr):
    non_duplicate = 0

    for i in range(0, WORD_SIZE):
        sum_i_position_bits = 0
        x = 1 << i
        for j in range(len(arr)):
            if arr[j] & x:
                sum_i_position_bits += 1

        if sum_i_position_bits % 3:
            non_duplicate |= x

    return non_duplicate


assert get_non_duplicated_number([6, 1, 3, 3, 3, 6, 6]) == 1
assert get_non_duplicated_number([13, 19, 13, 13]) == 19

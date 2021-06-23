from typing import List

from test_framework import generic_test


def multiply(arr1: List[int], arr2: List[int]) -> List[int]:
    """Multiply two arbitary precision ints represented as arrays"""
    negative = False
    if arr1[0] < 0 and arr2[0] < 0:
        arr1[0] = -arr1[0]
        arr2[0] = -arr2[0]
        negative = False
    elif arr1[0] < 0:
        arr1[0] = -arr1[0]
        negative = True
    elif arr2[0] < 0:
        arr2[0] = -arr2[0]
        negative = True

    product = 0
    counter = 1
    for i in reversed(range(len(arr2))):
        place_counter = 1 
        curr_sum = 0
        carry = 0
        for j in reversed(range(len(arr1))):
            curr = (arr1[j] * arr2[i]) + carry
            if curr >= 10 and j != 0:
                carry = curr // 10
                curr %= 10
            else:
                carry = 0
            curr_sum += curr * place_counter
            place_counter *= 10

        # next sum is multiply of 10
        product += curr_sum * counter
        counter *= 10


    res =  [int(x) for x in list(str(product))]
    if negative:
        res[0] = -res[0]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))

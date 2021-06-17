from typing import List

from test_framework import generic_test


def plus_one(arr: List[int]) -> List[int]:
    # first increment the least significant digit
    arr[-1] += 1
    
    # go through increasingly most significant digits and if any of
    # them turn out to be 10, put a 0, and carry forward 1 (school maths)
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break

        arr[i] = 0
        arr[i - 1] += 1

    # check for the most significant digit
    if arr[0] == 10:
        arr[0] = 1
        # we append 0 because the most significant digit is already 10
        # but we have to return a list of digits
        arr.append(0)

    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))

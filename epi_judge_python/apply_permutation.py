from copy import deepcopy
from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], arr: List[int]) -> None:
    res = [False] * len(arr)
    for i, index in enumerate(perm):
        res[index] = arr[i]
    
    for i, each in enumerate(res):
        arr[i] = each

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))

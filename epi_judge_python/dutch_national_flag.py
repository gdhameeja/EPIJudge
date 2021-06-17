import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

"""
THIS IS TWO PASS SOLUTION
def dutch_flag_partition(pivot_index: int, arr: List[int]) -> None:
    pivot = arr[pivot_index]
    smaller = 0
    # move all elemeents smaller than pivot to start
    for i, each in enumerate(arr):
        if each < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1

    larger = len(arr) - 1
    # move all elements larger than pivot to end
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            # we won't have any more larger elements than the pivot left over
            # as we already moved all smaller elements to the start
            return
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
"""


def dutch_flag_partition(pivot_index: int, arr: List[int]) -> None:
    """ single pass solution """
    pivot = arr[pivot_index]
    smaller, equal, larger = 0, 0, len(arr) - 1
    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1
 
        # equal processes the array 
        equal += 1     

def dutch_flag_partition(pivot_index: int, arr: List[int]) -> None:
    pivot = arr[pivot_index]
    smaller = 0
    # move all elemeents smaller than pivot to start
    for i, each in enumerate(arr):
        if each < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1

    larger = len(arr) - 1
    # move all elements larger than pivot to end
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            # we won't have any more larger elements than the pivot left over
            # as we already moved all smaller elements to the start
            return
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

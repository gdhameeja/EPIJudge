from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    return find_primes(n)

def find_primes(n):
    """ find all primes upto n """
    all_nums = [-1] + list(range(1, n + 1))
    is_two = True
    while True:
        if is_two:
            smallest_prime = 2
            is_two = False
        else:
            smallest_prime = find_smallest_prime(all_nums, smallest_prime)

        if smallest_prime == False:
            return [x for x in all_nums if x != False][2:]

        mark_composite(all_nums, smallest_prime)

    return -1  # should not reach


def mark_composite(arr, n):
    i = 2 * n
    while i < len(arr):
        arr[i] = False
        i += n


def find_smallest_prime(arr, last_smallest_number):
    for i in range(last_smallest_number + 1, len(arr)):
        if arr[i] != False:
            return arr[i]

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))

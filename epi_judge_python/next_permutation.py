from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    perm = [str(x) for x in perm]
    num = int(''.join(perm))
    idx = len(perm) - 2
    while True:
        perm[-1], perm[idx] = perm[idx], perm[-1]
        if int(''.join(perm)) > num:
            return [int(x) for x in perm]
        else:
            # reset the entries
            perm[-1], perm[idx] = perm[idx], perm[-1]
            idx -= 1

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))

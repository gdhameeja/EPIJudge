from typing import List

from test_framework import generic_test


def can_reach_end(arr: List[int]) -> bool:
    furthest_index_can_reach, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_index_can_reach and furthest_index_can_reach < last_index:
        furthest_index_can_reach = max(furthest_index_can_reach, i + arr[i])
        i += 1
    
    return furthest_index_can_reach >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))

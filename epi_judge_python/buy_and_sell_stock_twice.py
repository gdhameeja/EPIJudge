from typing import List

from test_framework import generic_test

"""
Brute force approach O(n^4)
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_diff = 0
    for i, each in enumerate(prices):
        for j in range(i, len(prices)):
            for k in range(j, len(prices)):
                for l in range(k, len(prices)):
                    max_diff = max(max_diff, ((prices[l] - prices[k]) + (prices[j] - prices[i])))

    return max_diff
"""

"""
O(n^2). Iterate through prices and compute max diff for
0..i-1 and i..n-1 at every step. Index i is the day i.
The maximum profit that can be made is the sum of the maximum profit before day i
and the maximum profit after day i including day i
It reuses the buy and sell stock once algorithm to find the profit before day i and after day i
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    n = len(prices)
    max_diff = 0
    for i, stock_price in enumerate(prices):
        # get max diff for 0..i - 1
        diff1 = buy_and_sell_stock_once(prices, 0, i - 1)
        # get max diff for i..n-1
        diff2 = buy_and_sell_stock_once(prices, i, n - 1)
        max_diff = max(max_diff, diff1 + diff2)

    return max_diff


def buy_and_sell_stock_once(prices, i, j):
    min_so_far = float('inf')
    max_diff = 0
    for idx in range(i, j + 1):
        min_so_far = min(min_so_far, prices[idx])
        max_diff = max(max_diff, prices[idx] - min_so_far)

    return max_diff
"""


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))

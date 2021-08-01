from typing import List

from test_framework import generic_test

"""
def buy_and_sell_stock_once(prices: List[float]) -> float:
    "brute force solution"
    max_diff = 0
    for i, each in enumerate(prices):
        for j in range(i + 1, len(prices)):
            max_diff = max(max_diff, prices[j] - prices[i])

    return max_diff
"""

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_value_so_far = prices[0]
    max_diff = 0
    for i, each in enumerate(prices):
        if each - min_value_so_far > max_diff:
            max_diff = each - min_value_so_far

        if each < min_value_so_far:
            min_value_so_far = each

    return max_diff


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

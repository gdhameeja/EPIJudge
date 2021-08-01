from typing import List

from test_framework import generic_test

"""
Brute force approach
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_diff = 0
    for i, each in enumerate(prices):
        for j in range(i, len(prices)):
            for k in range(j, len(prices)):
                for l in range(k, len(prices)):
                    max_diff = max(max_diff, ((prices[l] - prices[k]) + (prices[j] - prices[i])))

    return max_diff
"""

def buy_and_sell_stock_once(prices):
    pass

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))

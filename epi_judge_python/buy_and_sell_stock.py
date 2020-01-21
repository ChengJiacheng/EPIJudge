from typing import List

from test_framework import generic_test
from sys import exit


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    min_current = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        
        max_profit = max([max_profit, prices[i]-min_current])
        min_current = min([min_current, prices[i]])
            
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

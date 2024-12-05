#!/usr/bin/python3
""" making change module """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    gives change given coins and total
    """
    ret = 0
    if total <= 0:
        return 0
    if not coins:
        return -1
    coins.sort(reverse=True)
    for denomination in coins:
        ret += total // denomination
        total = total % denomination
    if total:
        return -1
    return ret

#!/usr/bin/python3
"""Change making
"""


def makeChange(coins, total):
    """gives changes based on available coins left
    """
    if total <= 0:
        return 0
    rem = total
    icount = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            icount += 1
        else:
            coin_idx += 1
    return icount

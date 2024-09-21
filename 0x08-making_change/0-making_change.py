#!/usr/bin/python3
"""
details in pdf
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """

    if coins is None:
        return -1

    if total <= 0:
        return 0

    change = 0

    coins = sorted(coins)[::-1]

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1

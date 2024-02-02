#!/usr/bin/python3
"""
fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given
    amount total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The target amount to be achieved.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If total is 0 or less, return 0.
         If the total cannot be met by any number of coins you have,
         return -1.
    """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change

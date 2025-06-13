#!/usr/bin/python3
"""Making change module
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # dp[i] = min coins needed to make total i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

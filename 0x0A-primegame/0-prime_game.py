#!/usr/bin/python3
"""Prime game
"""


def isWinner(x, nums):
    """Determines the game winner
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    # Sieve of Eratosthenes
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    # Precompute number of primes up to each number
    prime_counts = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_counts[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

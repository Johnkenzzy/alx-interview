#!/usr/bin/python3
"""Defines the minOperations function"""


def minOperations(n: int) -> int:
    """Checks the minimum operations needed to result at n"""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

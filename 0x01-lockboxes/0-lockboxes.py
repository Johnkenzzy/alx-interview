#!/usr/bin/python3
"""Defines the canUnlockAll function"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Checks if all boxes can be unlocked"""
    opened = set([0])
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)

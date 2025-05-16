#!/usr/bin/python3
"""Defines the validUTF* function"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    remaining_bytes = 0

    for num in data:
        # Only use the least significant 8 bits
        byte = num & 0xFF

        if remaining_bytes == 0:
            if byte >> 7 == 0b0:
                # 1-byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:
                # 2-byte character (110xxxxx)
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                # 3-byte character (1110xxxx)
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                # 4-byte character (11110xxx)
                remaining_bytes = 3
            else:
                return False  # Invalid start byte
        else:
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            remaining_bytes -= 1

    return remaining_bytes == 0

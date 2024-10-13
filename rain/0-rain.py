#!/usr/bin/python3
"""
    calculate how many square units of water will be retained after it rains.
"""


def rain(walls):
    """rain function"""

    water = 0

    # Check if there are at least three walls or the list is empty
    if len(walls) < 3 or not walls:
        return 0

    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        water += min(left, right) - walls[i]

    return water

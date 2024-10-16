#!/usr/bin/python3
"""Alu-interview minimum operations"""
import math


def minOperations(n):
    """Min operations"""
    if n <= 1:
        return 0
    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i
    if n > 1:
        operations += n
    return operations

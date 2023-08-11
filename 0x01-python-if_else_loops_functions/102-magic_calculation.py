#!/usr/bin/python3
# 102-magic_calculation.py
# Gahima Aristote <gahimaaristote1@gmail.com.com>


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)

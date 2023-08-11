#!/usr/bin/python3
# 7-islower.py
# Gahima Aristote <gahimaaristote1@gmail.com.com>


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task
"""

def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    up_next = 'H'
    body = 'H'
    op = 0
    while len(body) < n:
        if n % len(body) == 0:
            op += 2
            up_next = body
            body += body
        else:
            op += 1
            body += up_next
    if len(body) != n:
        return 0
    return op

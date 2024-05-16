#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    m = [False for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if not m[i]:
            for j in range(i*i, n + 1, i):
                m[j] = True
    m[0] = m[1] = True
    c = 0
    for i in range(len(m)):
        if not m[i]:
            c += 1
        m[i] = c
    p1 = 0
    for n in nums:
        p1 += m[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
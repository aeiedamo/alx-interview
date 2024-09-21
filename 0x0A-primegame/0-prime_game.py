#!/usr/bin/python3
"""
details in pdf.
"""


def isWinner(x, nums):
    """
    to find whos the winner
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben, maria = 0, 0
    sortednums = sorted(nums)[-1]+1

    oneinX = [1 for x in range(sortednums)]
    lenX = len(oneinX)

    for i in range(2, lenX):
        for j in range(2, lenX):
            try:
                oneinX[j * i] = 0
            except (ValueError, IndexError):
                break

    for i in nums:
        if sum(oneinX[0:(i + 1)]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

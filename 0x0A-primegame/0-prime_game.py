#!/usr/bin/python3
"""
details in pdf.
"""


def isPrime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def PrimeInRange(end):
    """
    Find all primes in the range (2 to end).
    """
    return [n for n in range(2, end + 1) if isPrime(n)]

def isWinner(x, nums):
    """
    Determine the winner of the game.
    """
    winsCountMaria, winsCountBen = 0, 0

    for num in nums:
        primes = PrimeInRange(num)
        if not primes:
            winsCountBen += 1
            continue

        rounds = list(range(1, num + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            prime = primes.pop(0)
            rounds = [n for n in rounds if n % prime != 0]
            primes = [p for p in primes if p in rounds]
            turn = 1 - turn

        if turn == 0:
            winsCountBen += 1
        else:
            winsCountMaria += 1

    if winsCountMaria > winsCountBen:
        return "Maria"
    elif winsCountBen > winsCountMaria:
        return "Ben"
    else:
        return None

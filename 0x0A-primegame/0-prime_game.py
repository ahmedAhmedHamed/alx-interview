#!/usr/bin/python3
"""
prime game module
"""


def get_count_primes(n: int) -> int:
    """calculates number of primes using sieve."""
    nums = [i for i in range(2, n + 1)]
    count_primes = len(nums)
    for num in nums:
        if num == -1:
            continue
        mul = num
        while num * mul <= n:
            if nums[(num * mul) - 2] != -1:
                count_primes -= 1
                nums[(num * mul) - 2] = -1
            mul += 1
    return count_primes


def isWinner(x, nums):
    """
    keep a count of each player's wins
    loop over nums:
        a player's win is decided by whether the number
        of primes up to a num is odd or even.
        get the number using the sieve of Eratosthenes
    """
    odd_wins = 0
    even_wins = 0
    for num in nums:
        num_primes = get_count_primes(num)
        if num_primes % 2:
            odd_wins += 1
        else:
            even_wins += 1
    return 'Maria' if odd_wins > even_wins else 'Ben'

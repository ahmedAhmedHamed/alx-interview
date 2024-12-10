#!/usr/bin/python3
"""
prime game module
"""
from typing import List


def get_prime_count_array(n: int) -> List[int]:
    """get_prime_count_array using sieve of Eratosthenes."""
    nums = [i for i in range(2, n + 1)]
    for i in range(len(nums)):
        num = nums[i]
        if num == -1:
            continue
        mul = num
        while num * mul <= n:
            if nums[(num * mul) - 2] != 0:
                nums[(num * mul) - 2] = 0
            mul += 1
        nums[i] = 1
    return nums


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
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    nums_sorted = sorted(nums)
    prime_count_array = get_prime_count_array(nums[-1])
    for num in nums_sorted:
        if not isinstance(num, int):
            return None
        num_primes = 0
        for i in prime_count_array:
            num_primes += i
        if num_primes % 2:
            odd_wins += 1
        else:
            even_wins += 1
    if odd_wins == even_wins:
        return None
    return 'Maria' if odd_wins > even_wins else 'Ben'

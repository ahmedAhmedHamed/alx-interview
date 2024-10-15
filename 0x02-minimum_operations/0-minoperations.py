#!/usr/bin/python3
"""
n = 12
H => copy => paste (HH) => cope => paste(HHHH) => copy
=> paste(HHHHHHHH) => paste(HHHHHHHHHHHH)(done)
7 moves
also possible:
h => copy => paste => paste(HHH) => copy => paste(HHHHHH)
=> paste(HHHHHHHHH) => paste(HHHHHHHHHHHH)(done)
also 7 moves
prime factors of 12 are: 2 * 3 * 3
===
We start at one
we always need to copy (except for n = 1)
to get to any other prime number named X we need to paste
X - 1 times.
===
hypothesis: to get to any number
get its biggest prime factor.
divide the number by the factor
the amount of times we need to paste after that
is the result of the division - 1.
for the past example:
    we had n  = 12
    biggest prime factor of 12 is 3
    12 / 3 = 4
    we had to paste 3 times.
+++
for n = 9:
prime factors are: 3 * 3
9 / 3 = 3
we need to paste 2 times
and to get to 3 we need to:
copy the H (1)
paste two times. (3)
copy the 3H (4)
paste two times. (6)
+++
for 4
prime factors of 4 are: 2 * 2
to get to 2 we need to:
copy the H (1)
paste once (2)
copy the 2H (3)
paste once (4)
===
this seems to be the correct way to go about this.
how do we get the prime factors of a number?
we need to calculate prime numbers P starting from 2
and if the number is divisible by P we divide it by P
and continue until the number becomes a prime number.

+prime numbers other than 2 are always odd.
===
---
===
core algo:
starting number of operations is always 2 assuming the number isn't prime or 1
(one for initial copy, second for second copy)
1. get max prime factor of n named P.
2. add P - 1 to the amount of operations.
3. add  (n / P) - 1 to the amount of operations.
4. return the amount of operations.
+++
how to get max prime factor of a number n:
check if n is a prime factor:
if so return n.
check if n is divisible by 2:
if it is: divide it by 2
and repeat
otherwise:
for every odd number starting at 3
check if the odd number is prime
if it is prime:
check if it is n is divisible by it:
if so:
divide it by P, set the maxPrime and repeat
=== more cases:
n = 25
H => copy => paste (HH) until 5
copy x1 + paste x4 = 5
copy => paste x4
10 operations
"""
from math import sqrt


def is_prime(n: int) -> bool:
    for i in range(int(sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True


def get_max_prime_factor(n: int) -> int:
    # if not isinstance(n, int):
    #     return 0
    n = int(n)
    if n <= 0:
        return 0
    max_prime_factor = -1
    while not is_prime(n):
        if n % 2 == 0:
            n /= 2
            max_prime_factor = max(max_prime_factor, 2)
        else:
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    if is_prime(i):
                        n /= i
                        max_prime_factor = max(max_prime_factor, i)
    return max(max_prime_factor, n)


def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.
     Your text editor can execute only two operations in this file:
      Copy All and Paste. Given a number n, write a method that calculates
       the fewest number of operations
        needed to result in exactly n H characters in the file.

    """
    if n == 1:
        return 0
    if is_prime(n):
        return n
    ret = 2  # will always need to copy at least twice.
    max_prime_factor = get_max_prime_factor(n)
    ret += max_prime_factor - 1
    ret += int(n / max_prime_factor) - 1
    return int(ret)

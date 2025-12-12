# def is_prime(num):
#     divisibility = 0
#     num = abs(num)
#     if num == 2:
#         return True
#     elif num <= 1:
#         return False
#     num = num // 2
#     for i in range(1,num+1):
#         if num % i == 0:  # this means it's divisible
#             divisibility += 1
#     if divisibility <= 2:
#         return True
#     else:
#         return False
#
"""
A number n (> 1) is prime if it has no divisors other than 1 and itself.
If n has a divisor d, then it also has a divisor n/d, and one of those
two will always be ≤ √n. So you only ever need to check for divisors
from 2 up to √n. Anything bigger will have a matching smaller pair
you already checked.
"""

# def is_prime(num):
#     if num <= 1: return False
#     if num == 2: return True
#     if num % 2 == 0: return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0: return False
#     return True

import math


def is_prime(n):
    n = abs(n)  # make negatives work the same as positives

    if n <= 1:  # 0, 1, -1, etc. are not prime
        return False
    if n == 2:  # 2 is the only even prime
        return True
    if n % 2 == 0:  # any other even number is not prime
        return False

    # Now check odd numbers from 3 up to √n
    # range(start, stop, step) — step=2 skips even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False  # found a divisor → not prime

    return True  # no divisors found → prime
#

print(is_prime(int(input("Which number would you like to check if prime?"))))


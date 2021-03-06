"""
Project Euler Problem #27
==========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                                e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

def is_prime(n):
    n = abs(n)

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True 

def consecutive_primes(a, b):
    n = 0
    while is_prime(n*n + a * n + b):
        n += 1
    return n

best = 0
product = 0

for b in range(-999, 1000):
    if not is_prime(b):
        continue
    for a in range(-999, 1000):
        con = consecutive_primes(a, b)
        if con > best:
            best = con
            product = a*b

print(product)

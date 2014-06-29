"""
Project Euler Problem #12
==========================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7^th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

import math

def divisors(a):
    n = 0
    sqrt = math.floor(math.sqrt(a))
    for i in range(1, sqrt+1):
        if a % i == 0:
            n += 2

    if(sqrt * sqrt == a):
        n -= 1
    return n

number = 0
i = 1

while divisors(number) < 500:
    number += i
    i += 1

print(number)

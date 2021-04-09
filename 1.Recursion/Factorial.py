#!/usr/bin/env python3

def factorial(n):
    assert n >= 0 and int(n) == n, "Input should be of integer type"

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))

#Output
24

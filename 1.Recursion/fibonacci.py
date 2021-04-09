#!/usr/bin/env python3

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Input should be of integer type"

    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(4))

#Output
3

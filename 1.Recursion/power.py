#!/usr/bin/env python3

def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)


print(power(2, 3))

# Output
8

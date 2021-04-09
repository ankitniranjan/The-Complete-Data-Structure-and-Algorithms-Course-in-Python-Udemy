#!/usr/bin/env python3

def sum_of_digits(n):
    assert n>=0 and int(n)==n, "Input should be integer"

    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(n/10)


print(sum_of_digits(122))


#Output
5

import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

import math

n = int(input())

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def divisor(fac):
    temp = 1
    for i in range(len(fac)):
        temp *= (fac[i][1] + 1)
    return temp

print(divisor(factorize(math.factorial(n))) % 1000000007)

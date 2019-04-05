import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))

m = a[0]

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

def lcm(a, b):
    "gcd関数を必要とする"
    return (a * b) // gcd(a,b)

for i in range(n):
    m = lcm(m,a[i])

m -= 1

ans = 0

for i in range(n):
    ans += m % a[i]

print(ans)

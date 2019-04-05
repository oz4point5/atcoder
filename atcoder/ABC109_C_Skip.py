import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

N,X = map(int,input().split())
x = list(map(int,input().split()))

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

length = []

for i in range(N):
    length.append(abs(x[i] - X))

ans = length[0]

for i in range(1,N):
    ans = gcd(ans,length[i])

print(ans)

import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

a.sort()
a.reverse()

alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice-bob)

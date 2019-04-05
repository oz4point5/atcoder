import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n, k = map(int,input().split())

odd = n // k
even1 = n // k
even2 = (n + int(k/2)) // k

if k % 2 == 0:
    print(even1 ** 3 + even2 ** 3)
else:
    print(odd ** 3)

import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

import statistics

n = int(input())
a = list(map(int,input().split()))

b = []

for i in range(n):
    b.append(a[i]-i)

bf = int(statistics.median(b))

ans = 0

for i in range(n):
    ans += abs(a[i] - bf - i)

print(ans)

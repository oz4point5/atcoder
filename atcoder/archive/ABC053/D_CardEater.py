import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC053/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

a.sort()


temp = 0
double = 0

for i in range(n):
    if temp != a[i]:
        temp = a[i]
    else:
        double += 1

if (n - double) % 2 == 0:
    print(n-double-1)
else:
    print(n-double)

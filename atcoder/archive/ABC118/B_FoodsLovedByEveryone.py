import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,m = map(int,input().split())
k = [0]
a = [[0]*(n+1)]*(n+1)
for i in range(1,n+1):
    raw = list(map(int,input().split()))
    k.append(raw[0])
    tmp = [0] + raw[1:]
    a[i] = tmp

all_a = []
for i in range(1,n+1):
    all_a += a[i]

all_a.sort()
rev_a = all_a[:]
rev_a.reverse()
ans = 0

for i in range(1,m+1):
    try:
         if n == (len(all_a) - rev_a.index(i)) - all_a.index(i):
             ans += 1
    except ValueError:
         pass

print(ans)

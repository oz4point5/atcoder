import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

k,s = map(int,input().split())

ans = 0

for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if 0 <= z <= k:
            ans += 1

print(ans)

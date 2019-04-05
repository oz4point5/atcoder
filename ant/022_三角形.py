import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

ans = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            len = a[i] + a[j] + a[k]
            ma = max(a[i], a[j], a[k])
            rest = len - ma
            if ma < rest:
                ans = max(ans, len)

print(ans)

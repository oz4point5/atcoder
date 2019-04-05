import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
r = int(input())
x = list(map(int,input().split()))
point = [False] * n
cover = 0
ans = 0

for i in range(n):
    if cover < x[i]:
        for j in range(i,n):
            if cover + r < x[j]:
                ans += 1
                point[j-1] = True
                cover = x[j-1] + r

print(ans)

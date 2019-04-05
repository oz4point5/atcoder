import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

N, M = map(int,input().split())
ABdic = dict()
for i in range(0,N):
    a,b = map(int,input().split())
    ABdic[a] = b

ans = 0
ABdic = sorted(ABdic.items(), key=lambda x:x[0])

for index, item in enumerate(ABdic):
    buy = 0
    if ABdic[index][1] > M:
        buy = M
    else:
        buy = ABdic[index][1]
    M -= buy
    ans += buy * ABdic[index][0]
    if M == 0:
        break

print(ans)

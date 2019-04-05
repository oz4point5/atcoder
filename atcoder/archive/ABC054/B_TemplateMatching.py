import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC054/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,m = map(int,input().split())
a = [i for i in range(n+1)]
b = [i for i in range(m+1)]
for i in range(1,n+1):
    a[i] = list(input())
for i in range(1,m+1):
    b[i] = list(input())
ans = True

for x in range(1,len(a[1])-len(b[1]) + 1 + 1):
    for y in range(1,len(a)-len(b) + 1 + 1):
        for ax in range(1,m+1):
            for ay in range(m):
                if a[ax][ay] != b[ax][ay]:
                    ans = False
                    break
            else:
                ans = True

if ans:
    print("Yes")
else:
    print("No")

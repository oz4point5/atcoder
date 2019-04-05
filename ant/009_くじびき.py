import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
m = int(input())
k = list(map(int,input().split()))

f = False

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if k[a] + k[b] + k[c] + k[d] == m:
                    f = True

if f == True:
    print("Yes")
else:
    print("No")

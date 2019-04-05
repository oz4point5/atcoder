import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

V = [1, 5, 10, 50, 100, 500]

C = list(map(int,input().split()))
A = int(input())

ans = 0

for i in range(6):
    j = 5 - i
    t = min(int(A / V[j]), C[j])
    A -= t * V[j]
    ans += t

print(ans)

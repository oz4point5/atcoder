import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
n = int(input())
a = [[0] for _ in range(2)]
for i in range(2):
    a[i] = list(map(int,input().split()))

ans = 0

for i in range(n):
    candy = 0
    candy += sum(a[0][:i+1])
    candy += sum(a[1][i:])
    ans = max(ans,candy)

print(ans)

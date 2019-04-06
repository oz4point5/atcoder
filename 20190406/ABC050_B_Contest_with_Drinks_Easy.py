import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
n = int(input())
t = list(map(int,input().split()))
m = int(input())
p = [0] * m
x = [0] * m
for i in range(m):
    p[i],x[i] = map(int,input().split())

all_time = sum(t)

for i in range(m):
    print(all_time - t[p[i]-1] + x[i])

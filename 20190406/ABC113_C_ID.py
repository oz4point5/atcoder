import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,m = map(int,input().split())
p = [0] * m
y = [0] * m
for i in range(m):
    p[i],y[i] = map(int,input().split())

certificate = [[] for _ in range(n)]

for i in range(m):
    certificate[p[i]-1].append(y[i])

for i in range(len(certificate)):
    certificate[i].sort()

for i in range(m):
    number = ""
    number += str(p[i]).zfill(6)
    number += str(certificate[p[i]-1].index(y[i])+1).zfill(6)
    print(number)

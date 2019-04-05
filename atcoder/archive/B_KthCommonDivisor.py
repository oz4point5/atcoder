import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b,k = map(int,input().split())
acd = []
bcd = []
cd = []

for i in range(1,a+1):
    if a % i == 0:
        acd.append(i)
for i in range(1,b+1):
    if b % i == 0:
        bcd.append(i)
for i in acd:
    for j in bcd:
        if i == j:
            cd.append(i)
print(cd[-k])

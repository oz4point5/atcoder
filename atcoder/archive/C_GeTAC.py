import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,q = map(int,input().split())
s = input()
lr = []
for i in range(0,q):
    lr.append(input().split())
map(int,lr)

ei = []
for index, item in enumerate(s):
    if index == n - 1:
        break
    if s[index] == "A" and s[index + 1] == "C":
        ei.append(index)

for i in range(0,q):
    sum = 0
    for j in range(int(lr[i][0])-1,int(lr[i][1])):
        if j in ei:
            sum += 1
    if int(lr[i][1])-1 in ei:
        sum -= 1
    print(sum)

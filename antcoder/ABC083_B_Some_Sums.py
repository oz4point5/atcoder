import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,a,b = map(int,input().split())

def digit_list(num):
    num = str(num)
    num = list(num)
    num = list(map(int,num))
    return num

cnt = 0

for i in range(1,n+1):
    temp = sum(digit_list(i))
    if a <= temp <= b:
        cnt += i

print(cnt)

import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC093/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b,k = map(int,input().split())
lists = []

for i in range(a,min(a+k,b+1)):
    lists.append(i)

for i in range(b,max(b-k,a),-1):
    lists.append(i)

l = set(lists)
m = list(l)

m.sort()

for i in m:
    print(i)

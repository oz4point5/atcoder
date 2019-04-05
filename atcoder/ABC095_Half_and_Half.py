import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
sl=l[:]
sl.sort()
a=sl[n//2-1]
b=sl[n//2]
for i in l:
  if i<=a:
    print(b)
  else:
    print(a)

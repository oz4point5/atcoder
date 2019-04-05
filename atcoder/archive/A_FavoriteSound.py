import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b,c = map(int,input().split())

ring = 0

while ring < c:
    if a <= b:
        b -= a
        ring += 1
    else:
        break

print(ring)

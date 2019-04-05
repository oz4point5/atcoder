import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
result = False

h,w = map(int,input().split())
c = [[0] * w] * h
c_reached =  [[False] * w] * h
for i in range(0,h):
    c[i] = list(input())


for i in range(0,h):
    for j in range(0,w):
        if c[i][j] == "s" :
            sx = int(i)
            sy = int(j)

def search(x,y):
    if x < 0 or w <= x or y < 0 or h <= y or c[x][y] == "#":
        return
    if c_reached[x][y]:
        return
    if c[x][y] == "g":
        result = True
    c_reached[x][y] = True
    search(x-1,y)
    search(x+1,y)
    search(x,y+1)
    search(x,y-1)

search(sx,sy)

if result:
    print("YES")
else:
    print("NO")

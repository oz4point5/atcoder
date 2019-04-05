import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

h, w = map(int, input().split())
c = [[0]*w for _ in range(h)]
start = [0, 0]
for i in range(h):
    c[i] = list(input())
    for j in range(w):
        if c[i][j] == "s":
            start = [i, j]

check = [[0]*w for _ in range(h)]

def search(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if c[y][x] == "#":
        return False
    if check[y][x] == 1:
        return False
    if c[y][x] == "g":
        return True
    check[y][x] = 1

    if search(x+1, y):
        return True
    if search(x-1, y):
        return True
    if search(x, y+1):
        return True
    if search(x, y-1):
        return True
    return False

if search(start[1], start[0]):
    print("Yes")
else:
    print("No")

import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

h,w = map(int,input().split())
c = [[0] for _ in range(h)]
for i in range(h):
    c[i] = list(input())
checked = [[0] * w for _ in range(h)]

def searchs(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "s":
                return [j,i]

ans = False
def dfs(x,y):
    global ans,checked
    if c[y][x] == "g":
        ans = True
        return

    checked[y][x] = 1

    for i in range(-1,2):
        for j in range(-1,2):
            if i == j:
                continue
            else:
                if 0 <= x + i < w and 0 <= y + j < h:
                    if c[y + j][x + i] != "#" and checked[y+j][x+i] == 0:
                        dfs(x+i,y+j)
    return

start = searchs(c)
dfs(start[0],start[1])

if ans:
    print("Yes")
else:
    print("No")

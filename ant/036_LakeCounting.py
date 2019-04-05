import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,m = map(int,input().split())
field = [[0] * n] * m

try:
    for i in range(m):
        field[i] = list(input())
except EOFError:
    pass

del field[10:]

def dfs(x,y):
    field[x][y] = "."
    for dx in range(-1,2):
        for dy in range(-1,2):
            nx,ny = x + dx, y + dy
            if 0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] == "W":
                dfs(nx, ny)
    return

res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == "W":
            dfs(i,j)
            res += 1
print(res)

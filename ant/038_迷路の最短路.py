import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

from collections import deque

INF = 100000000

N,M = map(int,input().split())
maze = [[0] * N] * M
for i in range(M):
    maze[i] = list(input())
for i in range(M):
    for j in range(N):
        if maze[i][j] == "S":
            sx,sy = j,i
        if maze[i][j] == "G":
            gx,gy = j,i

d = [[INF] * N] * M

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = deque()
    for i in range(N):
        for j in range(M):
            d[i][j] = INF
    que.append((sx,sy))
    d[sx][sy] = 0
    while len(que) :
        p = ()
        p = que.popleft()
        if (p[0] == gx and p[1] == gy):
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != "#" and d[nx][ny] == INF:
                que.append((nx,ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

res = bfs()
print(res)

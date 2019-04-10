import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# 入力
N,M = map(int,input().split())
field = [[0]*M for _ in range(N)]
for i in range(N):
    field[i] = list(input())

# 現在位置(x,y)
def dfs(x,y):
    # 今いるところを.に置き換える
    field[x][y] = "."

    # 移動する8方向をループ
    for dx in range(-1,2):
        for dy in range(-1,2):
            # x方向にdx y方向にdy移動した場所を(nx,ny)とする
            nx,ny = x + dx, y + dy

            # nxとnyが庭の範囲内かどうかとfield[nx][ny]が水たまりかどうかを判定
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == "W":
                dfs(nx,ny)

    return

res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == "W":
            # Wが残っているならそこからdfsをはじめる
            dfs(i,j)
            res += 1

print(res)

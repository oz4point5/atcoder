import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

from queue import Queue

INF = 100000000

# 状態を表すクラスpairの場合、typedefしておくと便利

# 入力
N,M = map(int,input().split())
maze = [[0] * N for _ in range(M)]      # 迷路を表す文字列の配列
for i in range(M):
    maze[i] = list(input())
    for j in range(N):
        if maze[i][j] == "S":
            sx = j                      # スタートの座標
            sy = i
        elif maze[i][j] == "G":
            gx = j                      # ゴールの座標
            gy = i

d = [[0] * N for _ in range(M)]         # 各点までの最短距離の配列

# 移動4方向のベクトル
dx,dy = [1,0,-1,0],[0,1,0,-1]

# (sx, sy)から(gx, gy)への最短距離を求める
# 辿り着けないとINF
def bfs():
    global d
    que = Queue()
    # すべての点をINFで初期化
    for i in range(N):
        for j in range(M):
            d[j][i] = INF
    # スタート地点をキューに入れ、その点の距離を0にする
    que.put([sx,sy])
    d[sy][sx] = 0

    # キューが空になるまでループ
    while not que.empty():
        p = []
        # キューの先頭を取り出す
        p = que.get()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx and p[1] == gy:
            break

        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点をnx, nyとする
            nx,ny = p[0] + dx[i], p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定（d[nx][ny] != INF なら訪れたことがある）
            if 0 <= nx < N and 0 <= ny < M and maze[ny][nx] != "#" and d[ny][nx] == INF:
                # 移動できるならキューに入れ、その点の距離をpからの距離+1で確定する
                que.put([nx,ny])
                d[ny][nx] = d[p[1]][p[0]] + 1

    return d[gy][gx]

res = bfs()
print(res)

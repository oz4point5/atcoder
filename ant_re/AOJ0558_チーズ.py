import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

from queue import Queue

h,w,n = map(int,input().split())
map = [[0] * w for _ in range(h)]
for i in range(h):
    map[i] = list(input())

que = Queue()
ans = 0
checked = [[-1] * w for _ in range(h)]

def bfs():
    global que,ans,checked
    while not que.empty():
        xy = que.get()
        if xy[0] == g[0] and xy[1] == g[1]:
            ans = checked[xy[1]][xy[0]]
            return
        for i in range(-1,2):
            for j in range(-1,2):
                if i == j or i == -j:
                    continue
                else:
                    if 0 <= xy[0] + i < w and 0 <= xy[1] + j < h:
                        if checked[xy[1]+j][xy[0]+i] == -1 and map[xy[1]+j][xy[0]+i] != "X":
                            checked[xy[1]+j][xy[0]+i] = checked[xy[1]][xy[0]] + 1
                            que.put([xy[0]+i,xy[1]+j])

mark = [[0,0] for _ in range(n+1)]
for i in range(h):
    for j in range(w):
        for k in range(1,n+1):
            if map[i][j] == str(k):
                mark[k] = [j,i]
            elif map[i][j] == "S":
                mark[0] = [j,i]

cnt = 0
for i in range(1,len(mark)):
    que = Queue()
    que.put([mark[i-1][0],mark[i-1][1]])
    g = [mark[i][0],mark[i][1]]
    ans = 0
    checked = [[-1] * w for _ in range(h)]
    checked[mark[i-1][1]][mark[i-1][0]] = 0
    bfs()
    cnt += ans

print(cnt)

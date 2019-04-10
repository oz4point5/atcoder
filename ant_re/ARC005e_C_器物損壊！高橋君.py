import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

from queue import Queue

h,w = map(int,input().split())
c = [[0] * w for _ in range(h)]
sx,sy,gx,gy = 0,0,0,0
for i in range(h):
    c[i] = list(input())
    for j in range(w):
        if c[i][j] == "s":
            sx,sy = j,i
        elif c[i][j] == "g":
            gx,gy = j,i

def bfs():
    global que,checked,ans
    while not que.empty():
        xy = que.get()
        if xy[0] == gx and xy[1] == gy:
            ans = True
            return
        for i in range(-1,2):
            for j in range(-1,2):
                if i == j or i == -j:
                    continue
                if 0 <= xy[0] + i < w and 0 <= xy[1] + j < h:
                    if checked[xy[1] + j][xy[0] + i] != 0:
                        if c[xy[1] + j][xy[0] + i] != "#":
                            if checked[xy[1]][xy[0]] < checked[xy[1] + j][xy[0] + i]:
                                checked[xy[1] + j][xy[0] + i] = checked[xy[1]][xy[0]]
                                que.put([xy[0] + i,xy[1] + j])
                        else:
                            if checked[xy[1]][xy[0]] < 2:
                                if checked[xy[1]][xy[0]] + 1 < checked[xy[1] + j][xy[0] + i] :
                                    checked[xy[1] + j][xy[0] + i] = checked[xy[1]][xy[0]] + 1
                                    que.put([xy[0] + i,xy[1] + j])

que = Queue()
checked = [[3] * w for _ in range(h)]
ans = False
checked[sy][sx] = 0
que.put([sy,sx])
bfs()
if ans:
    print("YES")
else:
    print("NO")

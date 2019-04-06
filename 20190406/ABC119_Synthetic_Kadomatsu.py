import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,a,b,c = map(int,input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())

l.sort()

print(l)

#深さ優先探索
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

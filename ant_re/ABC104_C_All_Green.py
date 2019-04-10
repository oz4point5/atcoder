import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
d,g = map(int,input().split())
p,c = [0] * d,[0] * d
for i in range(d):
    p[i],c[i] = map(int,input().split())

ans = float("inf")
def dfs(i, score, question, arr):
    global ans
    if i == d:
        if score >= g:
            ans = min(ans,question)
        else:
            arr.reverse()
            t = arr.index(0)
            t = d - t - 1
            if score + 100 * (t + 1) * p[t] > g:
                if (g - score) % (100 * (t + 1)) == 0:
                    ans = min(ans,question + int((g - score) / (100 * (t + 1))))
                else:
                    ans = min(ans,question + (g -score) // (100 * (t + 1)) + 1)
        return

    arr[i] = 0
    dfs(i + 1, score, question, arr)
    arr[i] = 1
    dfs(i + 1, score + (100 * (i + 1)) * p[i] + c[i], question + p[i], arr)

    return

array = [0] * d
dfs(0,0,0,array)

print(ans)

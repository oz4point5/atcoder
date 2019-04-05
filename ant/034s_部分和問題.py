import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))
k = int(input())

ans = False

def dfs (i, sum):
    global ans
    if sum == k:
        ans = True
    if i >= n:
        return
    dfs(i + 1, sum)
    dfs(i + 1, sum + a[i])

dfs(0,0)

if ans == True:
    print("Yes")
else:
    print("No")

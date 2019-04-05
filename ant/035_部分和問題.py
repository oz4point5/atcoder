import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def dfs(i , sum):
    if i == n:
        return sum == k
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False

if dfs(0,0):
    print("Yes")
else:
    print("No")

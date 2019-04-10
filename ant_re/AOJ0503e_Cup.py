import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
n,m = map(int,input().split())
abc = [[0] * n for _ in range(n)]
for i in range(0,n):
    abc[i] = list(map(int,input().split()))
    del abc[i][0]


print(n,m,abc)

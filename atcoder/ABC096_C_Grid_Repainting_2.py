import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

h,w = map(int,input().split())
s = [0]*(h+2)
s[0]= ["."]*(w+2)
for i in range(h):
    s[i+1] = ["."] + list(input()) + ["."]

ans = True
for i in range(1,h):
    for j in range(1,w):
        if s[i][j] == "#":
            if s[i-1][j] == "." and s[i+1][j] == "." and s[i][j-1] == "." and s[i][j+1] == ".":
                ans = False
                break

if ans:
    print("Yes")
else:
    print("No")

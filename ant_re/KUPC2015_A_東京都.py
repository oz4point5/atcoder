import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

t = int(input())
s = [0] * t
for i in range(t):
    s[i] = input()

cnt = 0
for i in range(t):
    ans = 0
    for j in range(len(s[i])):
        cnt -= 1
        if cnt < 0  and (s[i][j:j+5] == "kyoto" or s[i][j:j+5] == "tokyo"):
            ans += 1
            cnt = 4
    print(ans)

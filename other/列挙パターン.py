import sys
import os
f = open("C:/Users/user/Documents/python/other/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

cand = [1,2,3,4]

def dfs (i):
    if i <= 0:
        return [["1"],["2"],["3"],["4"]]
    temp = []
    for j in range(4**i):
        for k in range(4):
            tmp = dfs(i-1)[j] + list(str(cand[k]))
            temp.append(tmp)
    return temp

v = dfs(3)
str = ""

for i in range(len(v)):
    str += "".join(v[i]) + "\n"

print(str)

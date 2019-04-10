import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

abcd = list(input())
abcd = list(map(int,abcd))

ans = ""

def dfs(i, num, s):
    global ans
    if i == len(abcd):
        if num == 7:
            s += "=7"
            ans = s
        return

    dfs(i + 1, num + abcd[i], s + "+" + str(abcd[i]))
    dfs(i + 1, num - abcd[i], s + "-" + str(abcd[i]))

    return

dfs(1,abcd[0],str(abcd[0]))

print(ans)

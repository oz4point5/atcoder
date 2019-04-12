import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# 入力
N = int(input())
S = list(input())

# S[a], S[a+1], ..., S[b]が残っている文字列
a = 0
b = N - 1

while a <= b:
    left = False
    for i in range(b-a+1):
        if S[a + i] < S[b - i]:
            left = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break

    if left:
        print(S[a],end = "")
        a += 1
    else:
        print(S[b],end = "")
        b -= 1

print("")

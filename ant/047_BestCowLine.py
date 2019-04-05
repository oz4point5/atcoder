import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

N = int(input())
S = input().split()
S = list(*S)

a = 0
b = N - 1

str = ""

while(a <= b):
    left = False
    for i in range(0,b - a):
        if S[a + i] < S[b - i]:
            left = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break
    if left:
        str += S[a]
        a += 1
    else:
        str += S[b]
        b -= 1

print(str)

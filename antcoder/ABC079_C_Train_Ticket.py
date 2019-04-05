import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

abcd = list(input())
a = abcd[0]
b = abcd[1]
c = abcd[2]
d = abcd[3]

#bit全探索
n = 3
arr = [0] * n
for i in range(2 ** n):
    for j in range(n):
        if((1&i>>j) == 1):
            arr[j] = 1
        else:
            arr[j] = 0
    #ここに処理
    ia,ib,ic,id = int(a),int(b),int(c),int(d)
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        if ia + ib + ic + id == 7:
            print(a + "+" + b + "+" + c + "+" + d + "=7")
            break
    if arr[0] == 1 and arr[1] == 0 and arr[2] == 0:
        if ia - ib + ic + id == 7:
            print(a + "-" + b + "+" + c + "+" + d + "=7")
            break
    if arr[0] == 0 and arr[1] == 1 and arr[2] == 0:
        if ia + ib - ic + id == 7:
            print(a + "+" + b + "-" + c + "+" + d + "=7")
            break
    if arr[0] == 1 and arr[1] == 1 and arr[2] == 0:
        if ia - ib - ic + id == 7:
            print(a + "-" + b + "-" + c + "+" + d + "=7")
            break
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 1:
        if ia + ib + ic - id == 7:
            print(a + "+" + b + "+" + c + "-" + d + "=7")
            break
    if arr[0] == 1 and arr[1] == 0 and arr[2] == 1:
        if ia - ib + ic - id == 7:
            print(a + "-" + b + "+" + c + "-" + d + "=7")
            break
    if arr[0] == 0 and arr[1] == 1 and arr[2] == 1:
        if ia + ib - ic - id == 7:
            print(a + "+" + b + "-" + c + "-" + d + "=7")
            break
    if arr[0] == 1 and arr[1] == 1 and arr[2] == 1:
        if ia - ib - ic - id == 7:
            print(a + "-" + b + "-" + c + "-" + d + "=7")
            break

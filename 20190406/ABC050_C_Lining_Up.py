import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

a.sort()

can = True

if a[0] == 0:
    for i in range(1,n):
        if i % 2 != 1:
            if a[i] != i:
                can = False
                break
        else:
            if a[i] != i + 1:
                can = False
                break
    if can:
        print((2 ** int((n-1)/2))% (10 ** 9 + 7))
    else:
        print(0)
elif a[0] == 1:
    for i in range(0,n):
        if i % 2 != 1:
            if a[i] != i + 1:
                can = False
                break
        else:
            if a[i] != i:
                can = False
                break
    if can:
        print((2 ** int(n/2))% (10 ** 9 + 7))
    else:
        print(0)
else:
    print(0)

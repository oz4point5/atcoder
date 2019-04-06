import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

d,n = map(int,input().split())

if n <= 99:
    print(100 ** d * n)
else:
    print(100 ** d * 101)

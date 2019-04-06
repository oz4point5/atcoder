import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,m = map(int,input().split())

if n > int(m / 2):
    print(int(m/2))
else:
    parts = n * 2 + m
    print(int(parts/4))

import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

x = int(input())

length = 0
for i in range(10000000000):
    length += i
    if length >= x:
        print(i)
        break

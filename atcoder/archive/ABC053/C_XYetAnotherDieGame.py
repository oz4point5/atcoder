import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC053/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
import math

x = int(input())


temp = x // 11
move = temp * 2
if x % 11 == 0:
    pass
else:
    move += 1
    if x % 11 > 6:
        move += 1

print(move)

import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

x,y = map(int,input().split())

num = x
cnt = 0
while x <= y:
    x *= 2
    cnt += 1

print(cnt)

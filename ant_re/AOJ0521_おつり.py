import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

c = [500,100,50,10,5,1]

while True:
    n = int(input())
    if n == 0:
        break

    ch = 1000 - n
    ans = 0
    for i in range(6):
        num = int(ch / c[i])
        ans += num
        ch -= num * c[i]
    print(ans)

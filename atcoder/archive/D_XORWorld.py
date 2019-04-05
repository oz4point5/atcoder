import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b = map(int,input().split())
ans = a ^ (a + 1)
a += 1
while (a+1) < b:
    ans = ans ^ (a+1)
    a += 1
ans = ans ^ b
print(ans)

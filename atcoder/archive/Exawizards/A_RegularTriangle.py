import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/Exawizards/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())

if a == b == c:
    print("Yes")
else:
    print("No")

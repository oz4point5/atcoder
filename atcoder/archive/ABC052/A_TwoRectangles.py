import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b,c,d = map(int,input().split())

print(max(a*b,c*d))

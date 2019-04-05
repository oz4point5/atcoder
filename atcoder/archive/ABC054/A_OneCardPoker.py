import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC053/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b = map(int,input().split())

if a == 1:
    a = 14
if b == 1:
    b = 14

if a > b:
    print("Alice")
elif a == b:
    print("Draw")
else:
    print("Bob")

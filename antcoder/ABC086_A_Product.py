import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b = map(int,input().split())

if a * b % 2 == 1:
    print("Odd")
else:
    print("Even")

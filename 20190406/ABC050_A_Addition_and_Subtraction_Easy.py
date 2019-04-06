import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,op,b = input().split()
a,b = int(a),int(b)

if op == "+":
    print(a+b)
else:
    print(a-b)

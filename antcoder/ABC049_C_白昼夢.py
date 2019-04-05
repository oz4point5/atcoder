import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

s = list(input())

s.reverse()
s = "".join(s)

s = s.replace("maerd","A")
s = s.replace("remaerd","B")
s = s.replace("esare","C")
s = s.replace("resare","D")
s = s.replace("AC","")
s = s.replace("DA","")

if len(s) == 0:
    print("YES")
else:
    print("NO")

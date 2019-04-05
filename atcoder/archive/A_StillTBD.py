import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

y,m,d = map(int,input().split("/"))
if y < 2019:
    print("Heisei")
    print("Heisei")
elif y == 2019 and m < 4:
    print("Heisei")
elif y == 2019 and m == 4 and d <= 30:
    print("Heisei")
else:
    print("TBD")

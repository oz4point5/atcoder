import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

H,W = map(int,input().split())
h,w = map(int,input().split())

print(H*W-h*W-H*w+h*w)

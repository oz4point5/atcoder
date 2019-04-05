import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

import math

n,k = map(int,input().split())
a = list(map(int,input().split()))


print(math.ceil((n-1)/(k-1)))

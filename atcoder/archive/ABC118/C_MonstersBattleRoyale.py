import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

import math
from functools import reduce

n = int(input())
a = list(map(int,input().split()))
a = [0] + a

print(reduce(math.gcd, a[1:]))

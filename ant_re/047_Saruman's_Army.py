import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

N,R = map(int,input().split())
X = list(map(int,input().split()))

X.sort()

i,ans = 0,0
while i < N:
    # sはカバーされていない一番左の点の位置
    s = X[i]
    i += 1
    # sから距離Rを超える点まで進む
    while i < N and X[i] <= s + R:
        i += 1

    # pは新しく印をつける点のいち
    p = X[i - 1]
    # pから距離Rを超える点まで進む
    while i < N and X[i] <= p + R:
        i += 1

    ans += 1

print(ans)

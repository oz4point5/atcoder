import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# 入力
n = int(input())
a = list(map(int,input().split()))

ans = 0 # 答え

# 棒を重複して選ばないよう i < j < k となるようにしている
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            len = a[i] + a[j] + a[k]    # 周長
            ma = max(a[i],a[j],a[k])    # 最も長い棒の長さ
            rest = len - ma             # 他の2本の棒の長さの和

            if ma < rest:
                # 三角形が作れるので、答えを更新できれば更新
                ans = max(ans,len)

print(ans)

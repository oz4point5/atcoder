import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,k = map(int,input().split())
s = list(input())


def min_letter(arr):
    letter = "za"
    for i in range(len(arr)):
        if arr[i] < letter:
            letter = arr[i]
            num = i
    return num

for i in range(k):
    num = min_letter(s[i:])
    s[i],s[num+i] = s[num+i],s[i]

print("".join(s))

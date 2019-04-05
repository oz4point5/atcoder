import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
s = input().split()
s = list(*s)
sr = s[:]
sr.reverse()
str = ""

for i in range(0,n):
    if s[0] < sr[0]:
        str = str + s[0]
        del s[0]
        del sr[-1]
    elif s[0] > sr[0]:
        str = str + sr[0]
        del sr[0]
        del s[-1]
    else:
        if s < sr:
            str = str + s[0]
            del s[0]
            del sr[-1]
        else:
            str = str + sr[0]
            del sr[0]
            del s[-1]

print(str)

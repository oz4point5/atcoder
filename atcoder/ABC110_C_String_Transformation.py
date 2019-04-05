import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

s = list(input())
t = list(input())

s.sort()
t.sort()

def array_count(arr):
    arr_target = [[]]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            arr_target.append([arr[i-1],cnt])
            cnt = 1
    arr_target.append([arr[len(arr)-1],cnt])
    del arr_target[0]
    return arr_target

s = array_count(s)
t = array_count(t)

def get_item_1 (arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[i][1])
    return newarr

s = get_item_1(s)
t = get_item_1(t)

s.sort()
t.sort()

if s == t:
    print("Yes")
else:
    print("No")

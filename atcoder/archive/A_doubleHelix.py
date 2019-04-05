import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

b = input()

if b == "A":
    print("T")
if b == "T":
    print("A")
if b == "G":
    print("C")
if b == "C":
    print("G")

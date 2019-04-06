import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = input()
digit = len(n)
n = int(n)

def make753(num):
    cand = [""]
    endj = 0
    for i in range(num):
        for j in range(endj,3 ** i + endj):
            cand.append(cand[j] + "7")
            cand.append(cand[j] + "5")
            cand.append(cand[j] + "3")
            endj = j + 1
    del cand[0]
    return cand

cand = make753(digit)

delete = []
for i in range(len(cand)):
    if "3" not in cand[i] or "5" not in cand[i] or "7" not in cand[i]:
        delete.append(i)

diff = 0
for i in range(len(delete)):
    del cand[delete[i] - diff]
    diff += 1

for i in range(len(cand)):
    cand[i] = int(cand[i])

cand.sort()

for i in range(len(cand)):
    if n < cand[i]:
        print(i)
        break
else:
    print(len(cand))

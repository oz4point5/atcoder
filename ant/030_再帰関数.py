# -*- coding: utf-8 -*-

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

mem = [0] * 10000

def memfib(n):
    if n <= 1:
        return n
    if mem[n] != 0:
        return mem[n]
    mem[n] = memfib(n-1) + memfib(n-2)
    return mem[n]

print(memfib(6))

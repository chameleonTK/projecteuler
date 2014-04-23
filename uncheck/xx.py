# Python 2.6.4
# Project Euler, Problem 169
# Copyright 2010 Talha Zaman

from math import log
def f(n):
    split, unsplit, gap = 0, 0, 0
    for i in range(int(1+log(n, 2))):
        if n>>i&1 == 0: gap+=1
        else:
            if unsplit: unsplit, split = (1+gap)*unsplit + split, gap*unsplit + split
            else: unsplit, split = gap+1, gap
            gap = 0
    return unsplit

print f(int(raw_input()))
#print f(10**25)

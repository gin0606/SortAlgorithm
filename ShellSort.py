#!/usr/bin/env python
# -*- coding: utf-8; -*-

import random
from time import time

num = 1000

def init():
    li = []
    random.seed( int( time()))

    for x in range( 0, num ):
        li.append( int( random.random() * num ))

    return li

def sort( li ):
    liLen = len( li )
    # h[n+1]=3h[n]+1
    h = [ 1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,
          797161,2391484,7174453,21523360,64570081,193710244,
          581130733,1743392200,5230176601,15690529804,47071589413,
          141214768240,423644304721,1270932914164,3812798742493,
          11438396227480,34315188682441,102945566047324
          ]

    for i in range( 0, len( h ))[::-1]:
        if liLen > h[i]:
            j = 0
            while j + h[i] < liLen:
                k = j + h[i]
                while k < liLen:
                    if li[j] > li[k]:
                        li[j],  li[k] = li[k], li[j]
                    k = k + h[i]
                j += 1
        i -= 1

    return li


if __name__ == '__main__':
    t = time()
    print sort( init())
    print time() - t

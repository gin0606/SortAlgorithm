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
    listLen = len( li )

    for i in range( 0, listLen ):
        mi = i
        for j in range( i + 1, listLen ):
            if li[mi] > li[j]:
                mi = j
        li[i], li[mi] = li[mi], li[i]

    return li

if __name__ == '__main__':
    print sort( init())

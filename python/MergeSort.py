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

def mergeList( x, y ):
    ret = []
    xLen = len( x )
    yLen = len( y )
    i = 0
    j = 0

    while i < xLen and j < yLen:
        if x[i] < y[j]:
            ret.append( x[i] )
            i += 1
        else:
            ret.append( y[j] )
            j += 1

    while i < xLen:
        ret.append( x[i] )
        i += 1
    while j < yLen:
        ret.append( y[j] )
        j += 1

    return ret

def mergeSort( li ):
    liLen = len( li )

    if liLen == 1:
        ret = li
    else:
        div = int( liLen / 2 )

        left = mergeSort( li[0:div] )
        right = mergeSort( li[div:] )

        ret = mergeList( left, right )

    return ret

def sort( li ):
    return mergeSort( li )


if __name__ == '__main__':
    t = time()
    li = sort( init())
    t = time() - t
    print li
    print t

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


def quickSort( li ):
    liLen = len( li )
    if liLen < 1:
        return li

    pi = li[0]
    left = []
    right = []

    for i in range( 1, liLen ):
        if li[i] <= pi:
            left.append( li[i] )
        else:
            right.append( li[i] )

    left = quickSort( left )
    right = quickSort( right )

    return left + [pi] + right

def sort( li ):
    return quickSort( li )


if __name__ == '__main__':
    t = time()
    li = sort( init())
    t = time() - t
    print li
    print t

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
    i = 1

    while i < liLen:
        if li[i-1] > li[i]:
            li[i-1], li[i] = li[i], li[i-1]
            if i > 1:
                i -= 1
        else:
            i += 1

    return li


if __name__ == '__main__':
    t = time()
    print sort( init())
    print time() - t

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

    for i in range( 0, listLen - 1 ):
        j = i + 1
        tmp = li[j]
 
        for k in range( 0, j + 1 )[::-1]:
            if li[k-1] > tmp:
                li[k] = li[k-1]
            else:
                break
        li[k] = tmp

    return li


if __name__ == '__main__':
    t = time()
    print sort( init())
    print time() - t

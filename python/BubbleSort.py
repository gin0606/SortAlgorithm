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

def bubble( li ):
    listLen = len( li )

    for i in range( 0, listLen ):
        for j in range( i + 1, listLen ):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]

    return li

if __name__ == '__main__':
    t = time()
    print bubble( init())
    print time() - t

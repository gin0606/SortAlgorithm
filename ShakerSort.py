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
    head = 0
    tail = listLen - 1

    while head < tail:
        for i in range( head, tail ):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
        else:
            tail -= 1

        for i in range( head, tail )[::-1]:
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
        else:
            head += 1

    return li


if __name__ == '__main__':
    t = time()
    print sort( init())
    print time() - t

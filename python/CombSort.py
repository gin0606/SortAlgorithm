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
    h = int( liLen / 1.3 )

    while True:
        i = 0
        swa = False
        # Comb sort 11のアレ
        if 9 < h < 10:
            h = 11

        while i + h < liLen:
            if li[i] > li[i+h]:
                li[i], li[i+h] = li[i+h], li[i]
                swa = True
            i += 1

        if not swa:
            break
        else:
            h = int( h / 1.3 )

    return li


if __name__ == '__main__':
    t = time()
    print sort( init())
    print time() - t

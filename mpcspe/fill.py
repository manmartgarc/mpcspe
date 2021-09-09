# -*- coding: utf-8 -*-
"""
Created on Wednesday, 8th September 2021 9:40:33 pm
===============================================================================
@filename:  fill.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2017-18
@purpose:   uchicagoplacement.fill
===============================================================================
"""
from typing import List
import sys


def fill(a: List[int], i: int, v: int, x: int) -> None:
    if i < 0 or i >= len(a):
        return None
    if a[i] != v:
        return None
    elif a[i] == x:
        return None
    else:
        a[i] = x
        fill(a, i - 1, v, x)
        fill(a, i + 1, v, x)


def main(input: str):
    lines = input.split('\n')
    N, i, x = [int(x) for x in lines[0].split()]
    a = [int(x) for x in lines[1].split()]
    fill(a, i, a[i], x)
    sys.stdout.write(' '.join(str(val) for val in a))


if __name__ == "__main__":
    main(sys.stdin.read())

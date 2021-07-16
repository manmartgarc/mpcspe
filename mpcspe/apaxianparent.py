# -*- coding: utf-8 -*-
"""
Created on Wednesday, 9th June 2021 11:04:13 pm
===============================================================================
@filename:  honour_thy_parents.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   honor thy (apaxian) parent
===============================================================================
"""
import sys


def main(line: str):
    y, p = line.split()
    if y.endswith('e'):
        sys.stdout.write(''.join((y, 'x', p)))
    elif y[-1] in {'a', 'i', 'o', 'u'}:
        sys.stdout.write(''.join((y[:-1], 'ex', p)))
    elif y.endswith('ex'):
        sys.stdout.write(''.join((y, p)))
    else:
        sys.stdout.write(''.join((y, 'ex', p)))


if __name__ == "__main__":
    main(sys.stdin.read())

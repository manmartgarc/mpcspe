# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 7:13:19 pm
===============================================================================
@filename:  cgratio.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2017-18
@purpose:   cgratio
===============================================================================
"""
import sys


def main(line: str) -> None:
    lines = line.splitlines()

    total: int = 0
    cgs: int = 0
    for line in lines[1:]:
        total += len(line)
        cgs += line.count('C')
        cgs += line.count('G')

    result = (cgs / total) * 100

    sys.stdout.write(str(result))


if __name__ == "__main__":
    main(sys.stdin.read())

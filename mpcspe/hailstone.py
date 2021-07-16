# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 12:47:23 am
===============================================================================
@filename:  hailstone.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe 1819 - hailstone
@purpose:   hailstone code
===============================================================================
"""
import sys
from typing import List


def hailstone(x: int, elements: List[int]) -> int:
    x = int(x)
    elements.append(x)
    if x == 1:
        return 1
    else:
        if x % 2 == 0:
            return hailstone(x // 2, elements)
        else:
            return hailstone(3 * x + 1, elements)


def main(line: str) -> None:
    elements: List[int] = []
    hailstone(int(line.strip()), elements)
    sys.stdout.write(str(sum(elements)))


if __name__ == "__main__":
    main(sys.stdin.read())

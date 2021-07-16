# -*- coding: utf-8 -*-
"""
Created on Wednesday, 9th June 2021 11:29:44 pm
===============================================================================
@filename:  movingday.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   movingday
===============================================================================
"""
import sys


class Box:
    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self) -> int:
        return self.length * self.width * self.height


def main(line: str):
    lines = line.splitlines()
    diffs = []
    n, V = map(int, lines[0].split())
    for line in lines[1:]:
        l, w, h = map(int, line.split())
        box = Box(length=l, width=w, height=h)
        diffs.append(box.get_volume() - V)
    assert n == len(diffs)
    sys.stdout.write(str(max(diffs)))


if __name__ == "__main__":
    main(sys.stdin.read())

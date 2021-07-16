# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 3:23:48 pm
===============================================================================
@filename:  batterup.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   batterup
===============================================================================
"""
import sys


def main(line: str) -> None:
    lines = line.splitlines()
    inputs = list(map(int, lines[1].split()))
    inputs = [i for i in inputs if i >= 0]
    result = sum(inputs) / len(inputs)
    sys.stdout.write(str(result))


if __name__ == "__main__":
    main(sys.stdin.read())

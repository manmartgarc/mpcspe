# -*- coding: utf-8 -*-
"""
Created on Thursday, 15th July 2021 1:06:22 pm
===============================================================================
@filename:  test_main.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   enter project name
@purpose:   enter purpose
===============================================================================
"""
from pathlib import Path

import pytest


def load_tests() -> dict[str, str]:
    tdir = Path(__file__).parent.joinpath('tests')
    tfiles = tdir.glob('*.txt')
    iotests = {}

    for tfile in tfiles:
        with open(tfile, 'r') as f:
            for line in f.readlines():
                print(line.split('|'))

    return None


if __name__ == "__main__":
    load_tests()

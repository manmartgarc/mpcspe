# -*- coding: utf-8 -*-
"""
Created on Thursday, 15th July 2021 3:33:06 pm
===============================================================================
@filename:  loaders.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe
@purpose:   general purpose loading functions, primarily for testing
===============================================================================
"""
from __future__ import annotations

from pathlib import Path

import pkg_resources


def load_test_data(project: str) -> dict[str, str]:
    tdir = Path(
        pkg_resources.resource_filename('mpcspe', f'testdata/{project}'))

    ifiles = list(tdir.glob('in*.txt'))
    ofiles = list(tdir.glob('out*.txt'))

    if len(ifiles) != len(ofiles):
        raise ValueError(f'tests should be the same as outputs for {project}')

    tests = {}
    for infile, outfile in zip(ifiles, ofiles):
        with open(infile) as f:
            input = f.read()
        with open(outfile) as f:
            output = f.read()
        tests[input] = output

    return tests

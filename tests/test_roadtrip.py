# -*- coding: utf-8 -*-
"""
Created on Thursday, 15th July 2021 11:36:13 pm
===============================================================================
@filename:  test_roadtrip.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   unit tests for roadtrip
===============================================================================
"""
import io
from contextlib import redirect_stdout

import pytest
from mpcspe.loaders import load_test_data
from mpcspe.roadtrip import main

TEST_DATA = load_test_data('roadtrip')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_roadtrip(input, output):
    f = io.StringIO()
    output = output.strip()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert output == s

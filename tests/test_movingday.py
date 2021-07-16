# -*- coding: utf-8 -*-
"""
Created on Thursday, 15th July 2021 11:36:13 pm
===============================================================================
@filename:  test_movingday.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   unit tests for movingday
===============================================================================
"""
import io
from contextlib import redirect_stdout

import pytest
from mpcspe.loaders import load_test_data
from mpcspe.movingday import main

TEST_DATA = load_test_data('movingday')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_movingday(input, output):
    f = io.StringIO()
    output = int(output.strip())
    with redirect_stdout(f):
        main(input)
        s = int(f.getvalue())
        assert output == s

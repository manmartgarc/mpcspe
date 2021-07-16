# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 7:25:53 pm
===============================================================================
@filename:  test_cgratio.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2017-18
@purpose:   unit tests for cgratio
===============================================================================
"""
import io
import math
from contextlib import redirect_stdout

import pytest
from mpcspe.cgratio import main
from mpcspe.loaders import load_test_data

TEST_DATA = load_test_data('cgratio')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_cgratio(input, output):
    f = io.StringIO()
    output = output.strip()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert math.isclose(float(output), float(s), rel_tol=10e-3)

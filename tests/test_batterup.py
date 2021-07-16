# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 3:32:24 pm
===============================================================================
@filename:  test_batterup.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   unit tests for batterup
===============================================================================
"""
import io
from contextlib import redirect_stdout

import pytest
from mpcspe.loaders import load_test_data
from mpcspe.batterup import main

TEST_DATA = load_test_data('batterup')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_batterup(input, output):
    f = io.StringIO()
    output = output.strip()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert output == s

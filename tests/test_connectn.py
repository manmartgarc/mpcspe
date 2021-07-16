# -*- coding: utf-8 -*-
"""
Created on Thursday, 15th July 2021 10:56:59 pm
===============================================================================
@filename:  test_connectn.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe
@purpose:   connect-n unit test cases
===============================================================================
"""
from __future__ import annotations

import io
from contextlib import redirect_stdout

import pytest
from mpcspe.connectn import main
from mpcspe.loaders import load_test_data

TEST_DATA = load_test_data('connectn')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_connectn(input, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert output == s

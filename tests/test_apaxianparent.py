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
from __future__ import annotations

import io
from contextlib import redirect_stdout

import pytest
from mpcspe.apaxianparent import main
from mpcspe.loaders import load_test_data

TEST_DATA = load_test_data('apaxianparent')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_apaxianparent(input, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert output == s


if __name__ == "__main__":
    tests = load_test_data('apaxianparent')

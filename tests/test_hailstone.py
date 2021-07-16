# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 1:07:56 am
===============================================================================
@filename:  test_hailstone.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe
@purpose:   unit tests for hailstones
===============================================================================
"""
import io
from contextlib import redirect_stdout

import pytest
from mpcspe.hailstone import main
from mpcspe.loaders import load_test_data

TEST_DATA = load_test_data('hailstone')


@pytest.mark.parametrize(('input', 'output'), TEST_DATA.items())
def test_apaxianparent(input, output):
    f = io.StringIO()
    with redirect_stdout(f):
        main(input)
        s = f.getvalue()
        assert output == s


if __name__ == "__main__":
    tests = load_test_data('hailstone')

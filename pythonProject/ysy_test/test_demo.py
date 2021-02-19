#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:40
# @Author  : ysy
# @Site    : 
# @File    : test_demo.py
# @Software: PyCharm
import sys
import pytest

print(sys.path)
def inc(x):
    return x + 1
@pytest.mark.parametrize('a,b',[[3,4],[4,5],[5,6]])
def test_answer(a,b):
    assert inc(a) == b


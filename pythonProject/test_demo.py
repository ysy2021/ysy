#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:40
# @Author  : ysy
# @Site    : 
# @File    : test_demo.py
# @Software: PyCharm
import sys

print(sys.path)
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5
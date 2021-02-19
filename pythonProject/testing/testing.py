#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:40
# @Author  : ysy
# @Software: PyCharm
#=======模块/函数/方法/类取名=======
import sys
import pytest
print(sys.path)
#被测方法
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5
def test_answer1():
    assert inc(4) == 5
def test_answer2():
    assert inc(4) == 5
def test_answer22():
    assert inc(4) == 5
class test_t():
    def test_answer(self):
        assert inc(4) == 5

    def test_answer1(self):
        assert inc(4) == 5

    def test_answer2(self):
        assert inc(4) == 5

    @pytest.mark.run1
    def test_answer22(self):
        assert inc(4) == 5
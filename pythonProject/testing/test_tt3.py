#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/9 17:22
# @Author  : ysy
# @Software: PyCharm
from need.needtest import Calc

class Test_calc:
    def test_add(self):
        calc1=Calc()
        assert 3==calc1.add(1,2)

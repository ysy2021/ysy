#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 11:16
# @Author  : ysy
# @Software: PyCharm
import sys
import pytest
import yaml
print(11111111111111)
print(sys.path)
print(2222222222)
from calc_package.calculator import Calculator


def get_datas():
    with open('./datas/data.yml') as f:
        datas=yaml.safe_load(f)
        print(datas['add'])
        return datas

class Testcalc:
    def setup_class(self):
        print('测试开始咯')
    def teardown_class(self):
        print('测试结束')

    datas1=get_datas()
    @pytest.mark.parametrize('a,b,result',datas1['add'],ids=datas1['name'][0])
    def test_add(self,a,b,result):
        print(f'a= {a},b={b},result={result}')
        calc=Calculator()
        assert result==calc.add(a,b)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 20:40
# @Author  : ysy
# @Site    :
# @File    : test_demo.py
# @Software: PyCharm
#======setup/teardown  等使用
import sys
import pytest

print(sys.path)

#待测方法
def inc(x):
    return x + 1

def setup_module():
    print("测试模块开始执行")
def teardown_module():
    print("测试模块执行完成")
# def setup():
#     print("测试方法111开始执行")
# def teardown():
#     print("测试方法111结束执行")
def setup_function():
    print("测试函数开始执行")
def teardown_function():
    print("测试函数结束执行")


#测试函数
def test_answer():
    assert inc(4) == 3
def test_answer11():
    assert inc(4) == 5
def test_answer12():
    assert inc(4) == 5

#有标记的测试函数
@pytest.mark.run1
def test_answer13():
    assert inc(4) == 5
#测试类
class Test():
    def setup_class(self):
        print("测试类开始执行")
    def teardown_class(self):
        print("测试类结束执行")

    def setup_method(self):
        print("测试方法开始执行")
    def teardown_method(self):
        print("测试方法结束执行")
#测试方法
    def test_answer22(self):
        print("answer22执行中")
        assert inc(4) == 5
    def test_answer222(self):
        assert inc(4) == 5

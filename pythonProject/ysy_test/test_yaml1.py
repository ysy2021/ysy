#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 14:42
# @Author  : ysy
# @Software: PyCharm
import yaml


def test_yaml():

    with open('./datas/data.yml') as f:
        datas=yaml.safe_load(f)
        print(datas)
        print(datas['add'])
        print(datas['name'])
        return datas


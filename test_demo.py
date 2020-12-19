# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

class Testdemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open('./env.yaml')))
    def test_demo(self, env):
        if 'test' in env:
            print('测试')
            print(env)
        elif 'dev' in env:
            print('开发')

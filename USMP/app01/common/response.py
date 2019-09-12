#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/3下午2:42
# @Author :刘佩
# @Email  :2092357412@qq.com
# @File   :response.py

class CommonResponse():
    def __init__(self):
        """
        初始化
        """
        self.status = 200

    @property
    def get(self):
        """
        格式化成字典数据
        :return:
        """
        return self.__dict__

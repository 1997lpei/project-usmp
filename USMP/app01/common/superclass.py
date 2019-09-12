#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time  :2019/9/12下午2:11
# @Author :刘佩
# @Email  :2092357412@qq.com
# @File   :superclass.py
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View


class SuperView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        """
        重写dispatch方法   避免post请求无法进行csrf_token 验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(SuperView, self).dispatch(request, *args, **kwargs)


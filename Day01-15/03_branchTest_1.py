#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户身份验证
"""
username = input('请输入用户名：')
password = input('请输入口令：')
# 用户名为admin且密码为123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

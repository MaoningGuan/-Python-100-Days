#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百分制成绩转换为等级制成绩
"""
score = float(input('请输入成绩：'))
if score >=0 and score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('成绩对应的等级为：', grade)
else:
    print('请输入有效的成绩。')
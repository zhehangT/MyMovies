#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : t_zhehang
# Data : 17-1-19

import difflib


def get_only_chinese(check_str):
    result = ""
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            result += ch
    return result


t = u'史蒂夫.乔布斯.机器人生'
s1 = u'史蒂夫·乔布斯'
s2 = u'史蒂夫·乔布斯：机器人生'
s3 = u'iGenius：史蒂夫·乔布斯是如何改变世界的'

ss = [s1, s2, s3]

t= get_only_chinese(t)
for s in ss:
    s = get_only_chinese(s)
    seq = difflib.SequenceMatcher(None, t, s)
    print seq.ratio()




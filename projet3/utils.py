#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) JOHN PAUL (https://www.johnpaul.com/) all rights reserved.
# filename : utils
# date : 2019-12-07-08-59
# project: openclassroom_projet3
# author : alisaidomar
import operator

# "fat_100g'...




def make_filter(data_, *columns_, inv=True):

    # data = data[~data["fat_100"].isnull() & data["vita_100"].isnull()]
    if inv:
        op = operator.inv
    else:
        op = lambda x: x
    f = op(data_[columns_[0]].isnull())
    for c in columns_[1:]:
        f &= op( data_[c].isnull() )
    return f

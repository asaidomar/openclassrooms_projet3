#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : utils
# date : 2019-12-07-08-59
# project: openclassroom_projet3
# author : alisaidomar
import operator
import sys
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

# "fat_100g'...

def print_version():
    print("VERSION librairies")
    print('Python version ' + sys.version)
    print('Numpy version ' + np.__version__)
    print('Pandas version ' + pd.__version__)
    print('Matplotlib version ' + matplotlib.__version__ )
    print('Seaborn version ' + sns.__version__ )


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

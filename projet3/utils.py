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
import matplotlib.pyplot as plt


# "fat_100g'...

def print_version():
    print("VERSION librairies")
    print('Python version ' + sys.version)
    print('Numpy version ' + np.__version__)
    print('Pandas version ' + pd.__version__)
    print('Matplotlib version ' + matplotlib.__version__)
    print('Seaborn version ' + sns.__version__)


def make_filter(data_, *columns_, inv=True):
    # data = data[~data["fat_100"].isnull() & data["vita_100"].isnull()]
    if inv:
        op = operator.inv
    else:
        op = lambda x: x
    f = op((data_[columns_[0]].isnull()) | (data_[columns_[0]].isna()))
    for c in columns_[1:]:
        f &= op((data_[c].isnull()) | (data_[c].isna()))
    return f


def get_kcal(sample):
    new_sample = sample.copy()
    new_sample["lipide"] = (
            (new_sample["fat_100g"] +
             new_sample["saturated-fat_100g"]) * 9)
    new_sample["glucide"] = (
            (new_sample["sugars_100g"] +
             new_sample["carbohydrates_100g"]) * 4)
    new_sample["proteine"] = (new_sample["proteins_100g"] * 4)
    return new_sample[["lipide", "glucide", "proteine"]]


def get_metrics(data, codes, columns, columns_mg):
    # faire le ratio,
    for c in columns_mg:
        data[c] *= 1000
    sum_ = data[columns].mean()
    return sum_


def get_reference(data, columns, columns_mg):
    reference = data[(data["nutrition_grade_fr"] == "a")]
    # nutrition_score, nutrition_score_uk
    # reference = reference[utils.make_filter(reference, *columns)]
    for c in columns:
        reference = reference[(reference[c] <= 100) & (reference[c] >= 0)]
    for c in columns_mg:
        reference[c] *= 1000
    return reference[columns].mean()


def static_reference():
    """
    fat_100g               2.810923
    saturated-fat_100g     0.538446
    sugars_100g            3.766528
    carbohydrates_100g    24.213580
    proteins_100g          8.408718
    salt_100g              0.320081

    :return:
    """

    data = {"proteins_100g": 10, "fat_100g": 3,
            "saturated-fat_100g": 0.538446,
            'sugars_100g': 2, 'carbohydrates_100g': 24,
            "salt_100g": 1.2725}
    return pd.Series(data=data)


def plot_radar(current_data, columns, name="Composition"):
    labels = columns
    fig = plt.figure()
    stats_ = current_data

    angles = np.linspace(0, 2 * np.pi, len(columns), endpoint=False)

    stats = np.concatenate((stats_, [stats_[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    ax.set_title(name)
    ax.grid(True)

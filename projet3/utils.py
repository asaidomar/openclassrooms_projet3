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
    f = op((data_[columns_[0]].isnull())|(data_[columns_[0]].isna()))
    for c in columns_[1:]:
        f &= op((data_[c].isnull())|(data_[c].isna()))
    return f


def get_kcal(sample):
    new_sample = sample.copy()
    new_sample["lipide"] = (
            (new_sample["fat_100g"] +
             new_sample["saturated-fat_100g"] +
             new_sample["cholesterol_100g"] +
             new_sample["trans-fat_100g"]) * 9)
    new_sample["glucide"] = (
            (new_sample["sugars_100g"] +
             new_sample["carbohydrates_100g"]) * 4)
    new_sample["proteine"] = (new_sample["proteins_100g"] * 4)
    new_sample["alcohol"] = (new_sample["alcohol_100g"] * 4)
    return new_sample[["lipide", "glucide", "proteine", "alcohol"]]


def get_metrics(data, codes, columns, columns_mg):
    # faire le ratio,
    quantity = data["serving_quantity"]

    for c in columns_mg:
        data[c] *= 1000
    sum_ = data[columns].mean()
    return sum_


def get_reference(data, columns, columns_mg):
    reference = data[data["nutrition_grade_fr"] == "a"]
    # nutrition_score, nutrition_score_uk
    # reference = reference[utils.make_filter(reference, *columns)]
    for c in columns:
        reference = reference[(reference[c] <= 100) & (reference[c] >= 0)]
    for c in columns_mg:
        reference[c] *= 1000
    return reference[columns].mean()


def plot_radar(current_data, columns):
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
    name = "Composition"
    ax.set_title(name)
    ax.grid(True)
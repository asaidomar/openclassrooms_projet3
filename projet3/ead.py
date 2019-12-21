#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# filename : ead
# date : 2019-12-14-10-34
# project: openclassroom_projet3
# author : alisaidomar
# %%
import pandas as pd

from pathlib import Path

import projet3

# %%
# dossier data et resultats
data_folder = Path(projet3.__file__).with_name("data")
results_folder = Path(projet3.__file__).with_name("results")

# %%
# Chargement de la données brutes
data = data_folder / "en.openfoodfacts.org.products.csv"
data_df = pd.read_csv(data.as_posix(), sep="\t")

def get_data():
    return data_df

def get_columns_completude():
    # Nous allons calculer par colonnes le taux la complétude sur notre dataset
    completude_dict = {"Column": [], "Completude": []}
    # completude par colonne
    for c in data_df.columns:
        per_cent = len(data_df[~data_df[c].isnull()]) / len(data_df) * 100
        completude_dict["Column"].append(c)
        completude_dict["Completude"].append(per_cent)

    completude_df = pd.DataFrame(completude_dict)
    completude_df.to_csv(results_folder.joinpath("completude_columns.csv").as_posix())

    return completude_df


def get_completude_gt_than(completude_df, percent):
    # Pour quelle colonnes nous dispons de plus de 70 de complétude ?
    candidate_columns = completude_df[completude_df["Completude"] >= percent]
    return list(candidate_columns["Column"])


def get_completude_lt_than(completude_df, percent):
    # Pour quelle colonnes nous dispons de plus de 70 de complétude ?
    candidate_columns = completude_df[completude_df["Completude"] <= percent]
    return list(candidate_columns["Column"])


def generate_data_subset(candidate_columns):
    # Genaréation d'un subset de données basée sur les colonnes selectionnées précedemment
    data_subset = data_df[list(candidate_columns["Column"])]
    data_subset.info(verbose=True, null_counts=True)
    data_subset.to_csv(results_folder.joinpath("subset_data.csv"))

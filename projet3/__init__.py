#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# filename : __init__.py
# date : 2019-10-23-20-19
# project: openclassroom_projet3
# author : alisaidomar

# Selectionner un subset de colonnes
# supprimer les doublons


"""

 🎯Effectuer des opérations de nettoyage sur des données structurées

(Correlation je ne prends que les données fournies)
(Pour les données manquantes on peut prendre la médiane)
❒ Les éventuelles valeurs manquantes ont été mises en évidence. Une solution est proposée (elle doit être justifiée si plusieurs choix sont possibles).
❒ Une automatisation est réalisée :

    - utiliser les fonctions et méthodes (de pandas, numpy etc) adaptées si elles existent ;
    - éviter de copier-coller avec peu de modifications (penser aux boucles, dictionnaires).

(definition doublons, les lignes exactement semblables, )
❒ Les duplicats sont traités (de variables et d'enregistrements).
❒ Les variables non pertinentes pour la problématique de l'app ont été éliminées.



🎯Effectuer une analyse statistique univariée

❒ Des métriques adaptées sont employées (moyenne ou médiane selon la dispersion).

❒ Les éventuelles valeurs aberrantes ont été mises en évidence. Une solution est proposée (elle doit être justifiée si plusieurs choix sont possibles).

❒ Les distributions observées sont correctement caractérisées (uni, bi, multi-modale).

❒ La définition des quantiles est correctement maîtrisées. 



 🎯 Effectuer une analyse statistique multivariée

❒ La définition mathématique de la corrélation et les hypothèses sous-jacentes ont été expliquées

❒ Même distribution et corrélation ne sont pas confondues


🎯Communiquer ses résultats à l’aide de représentations graphiques lisibles et pertinentes
❒ Un graphe est utilisé à chaque fois que c'est nécessaire (ne pas décrire la distribution d'une variable sans graphe associé, par exemple !)

❒ Les graphes sont lisibles (taille de texte suffisante, bonne définition)

❒ Un graphique de chacun de ces types a été réalisé : boxplot, barplot, pie chart, histogramme, scatter plot



🎯Respect des consignes

❒ Les livrables sont complets

❒ Les livrables ont été déposés 48h à l'avance

❒ L'export de la base finale est présent dans le code

❒ Le temps de présentation est bien géré par l'étudiant 

"""


"""
calcium_100g
cholesterol_100g
trans-fat_100g
iron_100g
vitamin-c_100g
vitamin-a_100g

voir la répartition / au nom si c'est randaom
voir si c'est toujours les memes lignes qui sont manquantes
pour calcium voir les ligne de remplies

Depuis le code barre des aliments avoir les sueils et ce qui manque dans la composition du repas



3.2 La méthode de Hampel
Une autre méthode, dite de Hampel, consiste à considérer comme outliers les valeurs en dehors de l’intervalle constitué par la médiane, plus ou moins 3 déviation absolue de médiane :

I=[median–3∗mad;median+3∗mad]
Avec
mad=Median Absolute Deviation
et
mad=median(|yi–y~|)
et
y~=median(y)
"""



# TODO:
# les valeurs negatives trans_fat par ex
# regarder pk valeur uniques
# mettre les bons sueils pour les vitamines
# wrarnig sur les outiliers
# faire des rapport sur les outliers => les min max
# faire les boites à mouctaches pour voir les outilers



# correlation
# analyse bivariées


# depuis des codes barre analyser le contenu du 'repas'
# visualiser le contenu graphique du repas (les graphiques attendu)
# Un graphique de chacun de ces types a été réalisé : boxplot, barplot, pie chart, histogramme, scatter plot)
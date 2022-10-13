import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from scipy import stats

def MakeBoxPlotWithHue(x, y, hue, title, salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y],
                hue=salaries[hue])
    plt.show()


def MakeBoxPlotWithoutHue(x, y, title, salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y])
    plt.show()


def MakeBarWithoutHue(x, y, title, salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.barplot(x=salaries[x],
                y=salaries[y])
    plt.show()


def MakeBarWithHue(x, y, hue, title, salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.barplot(x=salaries[x],
                y=salaries[y],
                hue=salaries[hue])
    plt.show()

def makefacetboxplot(x, y, title, NA, EU, Asia):
    fig, ax = plt.subplots(figsize=(15, 7))

    plt.subplot(1, 3, 1)
    sns.boxplot(x=NA[x],
                y=NA[y])
    plt.title("North America")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 2)
    sns.boxplot(x=EU[x],
                y=EU[y])
    plt.title("Europe")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 3)
    sns.boxplot(x=Asia[x],
                y=Asia[y])
    plt.title("Asia")
    plt.xticks(rotation=90)

    plt.suptitle(title)
    plt.show()

def piegraph(colonne, title, salaries):
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.title(title)
    y = salaries[colonne].value_counts(dropna=False)
    mylabels = salaries[colonne].value_counts()
    plt.pie(y, labels=mylabels)
    plt.legend(salaries[colonne].value_counts().index, loc='upper left')
    plt.show()

# decris la table selon le salaire
def MakeTableDescribeWithSalary(toDescribe,data):
    print(data.groupby(toDescribe)[['salary_in_usd']].describe(include='all'))

def MakeKhi2Calcul(x, y, data):
    X = x
    Y = y
    cont = data[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)
    st_chi2, st_p, st_dof, st_exp = chi2_contingency(cont, correction=False)
    print("% d'assossiation selon le calcul de Khi2 :", st_p, '%')

def MakeCorrtestWithSpearmanrBetweenTwoInt(value1, value2, data, title):
    plt.scatter(data[value1], data[value2])
    plt.title(title)
    plt.show()
    print("Légende pour le table de corrélation entre ", value1, " et ", value2, stats.pearsonr(data[value1], data[value2]))

# pour faire corrélation entre un champ de string et un champ de int
def MakeCorrtestWithSpearmanrWithOneStringAndOneInt(valuestring, valueInt, data, title):
    cpt = 0
    position = 0
    arrayLegend = []
    arrayVerif = []
    shownArray = data[valuestring].values
    verif = 1
    for val in shownArray:
        for val2 in arrayVerif:
            if val2[0] == val:
                shownArray[position] = val2[1]
                verif = 0
        if verif == 1:
            arrayLegend.append(val+" : "+str(cpt))
            arrayVerif.append([val, cpt])
            shownArray[position] = cpt
            cpt = cpt + 1
        verif = 1
        position = position + 1
    plt.scatter(shownArray, data[valueInt])
    print("Légende pour le table de corrélation entre ", valuestring, " et ", valueInt, arrayLegend)
    plt.xticks(range(shownArray.min(), shownArray.max()+1))
    plt.title(title)
    plt.show()
    print("Légende pour le table de corrélation entre ", valuestring, " et ", valueInt, stats.pearsonr(shownArray, data[valueInt]))
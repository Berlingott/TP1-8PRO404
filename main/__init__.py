import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

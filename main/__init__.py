import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def MakeBoxPlotWithHue(x,y,hue,title,salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y],
                hue=salaries[hue])
    plt.show()

def MakeBoxPlotWithoutHue(x,y,title,salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y])
    plt.show()

def MakeBarWithoutHue(x,y,title,salaries):
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.barplot(x=salaries[x],
                y=salaries[y])
    plt.show()
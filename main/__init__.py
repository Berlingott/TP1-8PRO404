import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *
from scipy import stats


def make_boxplot_with_hue(x, y, hue, title, salaries):
    plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y],
                hue=salaries[hue])
    plt.show()


def make_boxplot_without_hue(x, y, title, salaries):
    plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.boxplot(x=salaries[x],
                y=salaries[y])
    plt.show()


def make_bar_without_hue(x, y, title, salaries):
    plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.barplot(x=salaries[x],
                y=salaries[y])
    plt.show()


def make_bar_with_hue(x, y, hue, title, salaries):
    plt.subplots(figsize=(15, 7))
    plt.title(title)
    sns.barplot(x=salaries[x],
                y=salaries[y],
                hue=salaries[hue])
    plt.show()


def make_facet_boxplot(x, y, title, north_america, europe, asia):
    plt.subplots(figsize=(15, 7))

    plt.subplot(1, 3, 1)
    sns.boxplot(x=north_america[x],
                y=north_america[y])
    plt.title("North America")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 2)
    sns.boxplot(x=europe[x],
                y=europe[y])
    plt.title("Europe")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 3)
    sns.boxplot(x=asia[x],
                y=asia[y])
    plt.title("Asia")
    plt.xticks(rotation=90)

    plt.suptitle(title)
    plt.show()


def pie_graph(column, title, salaries):
    plt.subplots(figsize=(10, 10))
    plt.title(title)
    y = salaries[column].value_counts(dropna=False)
    my_labels = salaries[column].value_counts()
    plt.pie(y, labels=my_labels)
    plt.legend(salaries[column].value_counts().index, loc='upper left')
    plt.show()


# Describes the table according to the salary
def make_table_describe_with_salary(to_describe, data):
    print(data.groupby(to_describe)[['salary_in_usd']].describe(include='all'))


def calculate_khi2(x, y, data):
    cont = data[[x, y]].pivot_table(index=x, columns=y, aggfunc=len).fillna(0).copy().astype(int)
    st_chi2, st_p, st_dof, st_exp = chi2_contingency(cont, correction=False)
    print("Pourcentage d'association selon le calcul de χ² : ", st_p, '%')


def make_corr_test_with_spearman_between_two_int(value1, value2, data, title):
    plt.scatter(data[value1], data[value2])
    plt.title(title)
    plt.show()
    print("Légende pour la table de corrélation entre ", value1, " et ", value2,
          stats.pearsonr(data[value1], data[value2]))


# To correlate between a string field and an integer field
def make_corr_test_with_spearman_with_one_string_and_one_int(value_string, value_int, data, title):
    counter = 0
    position = 0
    array_legend = []
    array_verification = []
    shown_array = data[value_string].values
    verif = 1
    for value in shown_array:
        for second_value in array_verification:
            if second_value[0] == value:
                shown_array[position] = second_value[1]
                verif = 0
        if verif == 1:
            array_legend.append(value + " : " + str(counter))
            array_verification.append([value, counter])
            shown_array[position] = counter
            counter = counter + 1
        verif = 1
        position = position + 1
    plt.scatter(shown_array, data[value_int])
    print("Légende pour la table de corrélation entre ", value_string, " et ", value_int, array_legend)
    plt.xticks(range(shown_array.min(), shown_array.max() + 1))
    plt.title(title)
    plt.show()
    print("Légende pour la table de corrélation entre ", value_string, " et ", value_int,
          stats.pearsonr(shown_array, data[value_int]))

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read salaries data
salaries = pd.read_csv("./../salaries.csv", header=0)

# affichage des 5 premières lignes
pd.set_option('display.max_columns', None) # pour l'affichage de toutes les colonnes
print(salaries.head()) # Print first 5 rows
print()

# get column names
print("VARIABLES")
for col in salaries.columns:
    print(col)
print()

# Return tuple with dimensionality of the dataframe
print("DIMENSIONS DU DATAFRAME")
print(salaries.shape)
print()

# Return serie with the data type of each column
print("TYPES DE VARIABLES")
print(salaries.dtypes)
print()

# Print informations about dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info())
print()

# count number of instances
print("NOMBRE D'INSTANCES")
index = salaries.index
print(len(index))      # 946 instances
print()

# get min and max values for each numeric column
print("MIN-MAX")
print("work_year")
print(salaries["work_year"].min(), salaries["work_year"].max())     #2020, 2022
print("salary")
print(salaries["salary"].min(), salaries["salary"].max())       #2324, 30400000
print("salary_in_usd")
print(salaries["salary_in_usd"].min(), salaries["salary_in_usd"].max())     #2324, 600000
print("remote_ratio")
print(salaries["remote_ratio"].min(), salaries["remote_ratio"].max())       #0, 100
print()

# Print descriptive statistics
print("SALARIES.DESCRIBE()")
print(salaries.describe())
print()

# print summary stats for dataset and import to excel
salaries.describe().to_excel("../statistic_description_salaries.xlsx")
# count total NaN per column
print("VALEURS NULLES PAR COLONNE")
print(salaries.isnull().sum())
print()

# Explore categorical data 
print("VARIABLES CATEGORIELLES")
print(salaries['work_year'].value_counts(dropna=False))
print()
print(salaries['experience_level'].value_counts(dropna=False))
print()
print(salaries['employment_type'].value_counts(dropna=False))
print()
print(salaries['job_title'].value_counts(dropna=False))
print()
print(salaries['salary_currency'].value_counts(dropna=False))
print()
print(salaries['employee_residence'].value_counts(dropna=False))
print()
print(salaries['remote_ratio'].value_counts(dropna=False))
print()
print(salaries['company_location'].value_counts(dropna=False))
print()
print(salaries['company_size'].value_counts(dropna=False))
print()

# Create dataframe with all the duplicated variables
df_dup=salaries[salaries.duplicated()]
# print number fo duplicates
print("NOMBRES DES DOUBLONS")
print(df_dup.shape)
print()

# print duplicates
print("APERÇU DES DOUBLONS")
print(df_dup)
print()

# extreme values
sns.boxplot(data=salaries['salary'])
# set y axis' values as non exponantial
plt.ticklabel_format(style='plain', axis='y')
plt.show()

sns.boxplot(data=salaries['salary_in_usd'])
# set y axis' values as non exponantial
plt.ticklabel_format(style='plain', axis='y')
plt.show()

print("VALEURS ABERRANTES ÉLEVÉES - SALARY_IN_USD")
print(salaries.loc[salaries.salary_in_usd > (salaries.salary_in_usd.mean() + 3*salaries.salary_in_usd.std())])
print()
print("VALEURS ABERRANTES INFÉRIEURES - SALARY_IN_USD < 20k")
print(salaries.loc[salaries.salary_in_usd <= 20000]) # (0 or (salaries.salary_in_usd.mean() - 3*salaries.salary_in_usd.std()))])
# note: sur toutes les entrés de moins de 20K, aucun n'est résident US...







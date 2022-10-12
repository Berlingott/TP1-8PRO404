# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


salaries = pd.read_excel("mods.xlsx", header=0)
pd.set_option('display.max_columns', None)
print(salaries.head())

# informations sur le dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info())
print()

# create grouped boxplot
sns.boxplot(x=salaries['employment_type'],
            y=salaries['salary_in_usd']) #,
            #hue=salaries['employee_continent'])
plt.show()
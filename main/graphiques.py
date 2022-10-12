# import modules
from pathlib import Path
import sys
from __init__ import *
from description_données_TP1 import *


salaries = pd.read_excel("../mods.xlsx", header=0)
pd.set_option('display.max_columns', None)
print(salaries.head())

# informations sur le dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info())
print()

# create grouped boxplot
MakeBoxPlotWithHue('job_category', 'salary_in_usd', 'company_continent', 'TEST TILE', salaries)
MakeBoxPlotWithoutHue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
MakeBarWithoutHue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
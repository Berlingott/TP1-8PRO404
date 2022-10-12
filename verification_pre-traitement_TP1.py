# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read salaries data
salaries = pd.read_csv("salaries.csv", header=0)

# affichage des 5 premières lignes
pd.set_option('display.max_columns', None)
# Retire la colonne salary et salary_currency
mods = salaries.drop(["salary", "salary_currency"], axis=1)

# Nouvelle colonne pour les catégories de métier
job_dictionary = {"Data Scientist": "DATA SCIENCE",
                  "Research Scientist": "DATA SCIENCE",
                  "Applied Data Scientist": "DATA SCIENCE",
                  "Data Specialist": "DATA SCIENCE",
                  "Applied Scientist": "DATA SCIENCE",
                  "Staff Data Scientist": "DATA SCIENCE",
                  "AI Scientist": "DATA SCIENCE",
                  "Data Science Consultant": "DATA SCIENCE",
                  "Principal Data Scientist": "DATA SCIENCE",
                  "Data Science Manager": "DATA SCIENCE",
                  "Data Manager": "DATA SCIENCE",
                  "Lead Data Scientist": "DATA SCIENCE",
                  "Head of Data": "DATA SCIENCE",
                  "Head of Data Science": "DATA SCIENCE",
                  "Director of Data Science": "DATA SCIENCE",
                  "Data Engineer": "DATA ENGINEERING",
                  "Data Operations Engineer": "DATA ENGINEERING",
                  "Data Science Engineer": "DATA ENGINEERING",
                  "Cloud Data Engineer": "DATA ENGINEERING",
                  "Principal Data Engineer": "DATA ENGINEERING",
                  "Data Engineering Manager": "DATA ENGINEERING",
                  "Lead Data Engineer": "DATA ENGINEERING",
                  "Director of Data Engineering": "DATA ENGINEERING",
                  "Data Analyst": "DATA ANALYSIS",
                  "Data Operations Analyst": "DATA ANALYSIS",
                  "Product Data Analyst": "DATA ANALYSIS",
                  "BI Data Analyst": "DATA ANALYSIS",
                  "Business Data Analyst": "DATA ANALYSIS",
                  "Marketing Data Analyst": "DATA ANALYSIS",
                  "Finance Data Analyst": "DATA ANALYSIS",
                  "Financial Data Analyst": "DATA ANALYSIS",
                  "Data Analytics Consultant": "DATA ANALYSIS",
                  "Analytics Engineer": "DATA ANALYSIS",
                  "Data Analytics Engineer": "DATA ANALYSIS",
                  "Principal Data Analyst": "DATA ANALYSIS",
                  "Lead Data Analyst": "DATA ANALYSIS",
                  "Data Analytics Lead": "DATA ANALYSIS",
                  "Data Analytics Manager": "DATA ANALYSIS",
                  "ML Engineer": "ML ENGINEERING",
                  "Machine Learning Research Engineer": "ML ENGINEERING",
                  "NLP Engineer": "ML ENGINEERING",
                  "Machine Learning Scientist": "ML ENGINEERING",
                  "Applied Machine Learning Scientist": "ML ENGINEERING",
                  "Machine Learning Infrastructure Engineer": "ML ENGINEERING",
                  "Machine Learning Developer": "ML ENGINEERING",
                  "Lead Machine Learning Engineer": "ML ENGINEERING",
                  "Machine Learning Manager": "ML ENGINEERING",
                  "Head of Machine Learning": "ML ENGINEERING",
                  "Machine Learning Engineer": "ML ENGINEERING",
                  "Data Architect": "DATA ARCHITECTURE",
                  "ETL Developer": "DATA ARCHITECTURE",
                  "Cloud Data Architect": "DATA ARCHITECTURE",
                  "Big Data Architect": "DATA ARCHITECTURE",
                  "Big Data Engineer": "DATA ARCHITECTURE",
                  "Computer Vision Engineer": "DATA ARCHITECTURE",
                  "Computer Vision Software Engineer": "DATA ARCHITECTURE",
                  "3D Computer Vision Researcher": "DATA ARCHITECTURE"}
mods['job_category'] = mods['job_title'].map(job_dictionary)

# Nouvelles colonnes pour la location des entreprises/employé par continents
continent_dictionary = {"AE": "Asia",
                        "AL": "Europe",
                        "AR": "South America",
                        "AS": "Oceania",
                        "AT": "Europe",
                        "AU": "Oceania",
                        "AX": "Europe",
                        "BE": "Europe",
                        "BG": "Europe",
                        "BO": "South America",
                        "BR": "South America",
                        "CA": "North America",
                        "CH": "Europe",
                        "CL": "South America",
                        "CN": "Asia",
                        "CO": "South America",
                        "CZ": "Europe",
                        "DE": "Europe",
                        "DK": "Europe",
                        "DO": "North America",
                        "DZ": "Africa",
                        "EE": "Europe",
                        "EG": "Africa",
                        "ES": "Europe",
                        "FI": "Europe",
                        "FR": "Europe",
                        "GB": "Europe",
                        "GR": "Europe",
                        "HK": "Asia",
                        "HN": "North America",
                        "HR": "Europe",
                        "HU": "Europe",
                        "ID": "Asia",
                        "IE": "Europe",
                        "IN": "Asia",
                        "IQ": "Asia",
                        "IR": "Asia",
                        "IT": "Europe",
                        "JE": "Europe",
                        "JP": "Asia",
                        "KE": "Africa",
                        "LU": "Europe",
                        "MD": "Europe",
                        "MT": "Europe",
                        "MX": "North America",
                        "MY": "Asia",
                        "NG": "Nigeria",
                        "NL": "Europe",
                        "NZ": "Oceania",
                        "PH": "Asia",
                        "PK": "Asia",
                        "PL": "Europe",
                        "PM": "North America",
                        "PR": "North America",
                        "PT": "Europe",
                        "RO": "Europe",
                        "RS": "Europe",
                        "RU": "Europe",
                        "SG": "Singapore",
                        "SI": "Europe",
                        "TH": "Asia",
                        "TN": "Africa",
                        "TR": "Asia",
                        "UA": "Europe",
                        "US": "North America",
                        "VN": "Asia"}
mods['employee_continent'] = mods['employee_residence'].map(continent_dictionary)
mods['company_continent'] = mods['company_location'].map(continent_dictionary)

# Filtre de données aberrantes.
filter_max = (mods.salary_in_usd.mean() + 3*mods.salary_in_usd.std())
for x in mods.index:
    if mods.loc[x, 'salary_in_usd'] > filter_max:
        mods.drop(x, inplace=True)
    elif mods.loc[x, 'salary_in_usd'] < 20000:
        mods.drop(x, inplace=True)
mods.drop_duplicates(inplace=True)

# Fichier excel mods. Conserver à la fin du code pour qu'il enregistre toute les mods
mods.to_excel("mods.xlsx")

# Compte des valeurs des nouvelles colonnes
print(mods['job_category'].value_counts())
print()
print(mods['employee_continent'].value_counts())
print()
print(mods['company_continent'].value_counts())

#Partie tableau David

fig, ax = plt.subplots(figsize=(15, 7))
plt.subplots_adjust(bottom=0.45)
plt.title(" Boxplot des différentes catégories de job et leurs salaires")
sns.boxplot(x=mods['job_category'],
            y=mods['salary_in_usd'],
            hue=mods['company_continent'])
plt.show()

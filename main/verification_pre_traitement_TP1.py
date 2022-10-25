# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def DataCleaning():
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
    # load data set with iso codes and continent
    countries = pd.read_csv("country_file.csv", header=0)
    # keep only relevant columns "C:\\Users\\vince\\PycharmProjects\\TP1-8PRO404\\salaries.csv"
    countries = countries[["alpha-2", "region"]]
    # add new column with region
    countries = countries.rename(columns={"alpha-2": "company_location", "region": "company_continent"})
    mods = pd.merge(mods, countries, on="company_location", how="inner")
    countries = countries.rename(columns={"company_location": "employee_residence", "company_continent": "employee_continent"})
    mods = pd.merge(mods, countries, on="employee_residence", how="inner")

    # # Filtre de données aberrantes.
    # filter_max = (mods.salary_in_usd.mean() + 3*mods.salary_in_usd.std())
    # for x in mods.index:
    #     if mods.loc[x, 'salary_in_usd'] > filter_max:
    #         mods.drop(x, inplace=True)
    #     elif mods.loc[x, 'salary_in_usd'] < 20000:
    #         mods.drop(x, inplace=True)
    # mods.drop_duplicates(inplace=True)

    # retirer les categories PT, CT et FL
    mods = mods.loc[(mods.employment_type == "FT")]
    print(mods['employment_type'].value_counts())

    # retirer des colones inutiles
    mods.drop(columns='employment_type', inplace=True)
    mods.drop(columns='employee_residence', inplace=True)
    mods.drop(columns='company_location', inplace=True)
    mods.drop(columns='job_title', inplace=True)
    # retrait des continents avec trop peu de donnees
    mods = mods.loc[(mods.employee_continent == "Americas") |
                    (mods.employee_continent == "Europe") |
                    (mods.employee_continent == "Asia")]

    mods = mods.loc[(mods.company_continent == "Americas") |
                    (mods.company_continent == "Europe") |
                    (mods.company_continent == "Asia")]
    # group salary_in_usd in interval
    # set condition
    conditions = [
        (mods['salary_in_usd'] < 30000),
        (mods['salary_in_usd'] >= 30000) & (mods['salary_in_usd'] < 60000),
        (mods['salary_in_usd'] >= 60000) & (mods['salary_in_usd'] < 90000),
        (mods['salary_in_usd'] >= 90000) & (mods['salary_in_usd'] < 120000),
        (mods['salary_in_usd'] >= 120000) & (mods['salary_in_usd'] < 150000),
        (mods['salary_in_usd'] >= 150000) & (mods['salary_in_usd'] < 180000),
        (mods['salary_in_usd'] >= 180000) & (mods['salary_in_usd'] < 210000),
        (mods['salary_in_usd'] >= 210000) & (mods['salary_in_usd'] < 240000),
        (mods['salary_in_usd'] >= 270000) & (mods['salary_in_usd'] < 300000),
        (mods['salary_in_usd'] >= 300000)
    ]
    # set values
    values = ["[0,30 000[", "[30 000, 60 000[", "[60 000, 90 000[", "[90 000, 120 000[", "[120 000, 150 000[", "[150 000, 180 000[", "[210 000, 240 000[", "[240 000, 270 000[", "[270 000, 300 000[", ">300 000"]# replace
    mods["salary_in_usd"] = np.select(conditions, values)
    # Fichier excel mods. Conserver à la fin du code pour qu'il enregistre toute les mods
    mods.to_csv("../mods.csv")



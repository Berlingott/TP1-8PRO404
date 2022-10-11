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

# Fichier exel mods garder à la fin du code pour qu'il enregistre toute les mods
mods.to_excel("mods.xlsx")
print(mods['job_category'].value_counts())
import numpy as np
import pandas as pd

filter_min = 20000

experience_dictionary = {"EN": "1-EN", "MI": "2-MI", "SE": "3-SE", "EX": "4-EX"}

colums_to_drop = ["salary", "salary_currency", "employment_type"]

# New column to categorize 'job_title'
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

# Set values used as labels for salary
salary_categorical_values = ["[0,50 000[", "[50 000, 100 000[", "[100 000, 150 000[", "[150 000, 200 000[",
                             "[200 000, 250 000[", "[250 000, 300 000[", ">300 000"]


def set_six_categorizing_conditions(my_df_dataset, column_name, interval):
    salary_refactoring_conditions = [
        (my_df_dataset[column_name] < interval),
        (my_df_dataset[column_name] >= interval) & (my_df_dataset[column_name] < interval * 2),
        (my_df_dataset[column_name] >= interval * 2) & (my_df_dataset[column_name] < interval * 3),
        (my_df_dataset[column_name] >= interval * 3) & (my_df_dataset[column_name] < interval * 4),
        (my_df_dataset[column_name] >= interval * 4) & (my_df_dataset[column_name] < interval * 5),
        (my_df_dataset[column_name] >= interval * 5) & (my_df_dataset[column_name] < interval * 6),
        (my_df_dataset[column_name] >= interval * 6)
    ]
    return salary_refactoring_conditions


def recategorize_from_dictionary(my_df_dataframe, dictionary, column_name, new_column_name):
    my_df_dataframe[new_column_name] = my_df_dataframe[column_name].map(dictionary)
    if column_name != new_column_name:
        my_df_dataframe.drop(columns=column_name, inplace=True)
    return my_df_dataframe


def recategorize_country_by_continent(my_df_dataframe, column_name, new_column_name):
    # Change the company and employee locations for continents
    # Load data set with ISO codes and continents
    countries = pd.read_csv("country_file.csv", header=0)
    # Keep only the relevant columns for 'salaries.csv'
    countries = countries[["alpha-2", "region"]]
    # Add new column with regions
    countries = countries.rename(
        columns={"alpha-2": column_name, "region": new_column_name})  # Rename to uniformize datasets
    my_df_dataframe = pd.merge(my_df_dataframe, countries, on=column_name, how="inner")
    my_df_dataframe.drop(columns=column_name, inplace=True)

    class_id = my_df_dataframe[new_column_name].value_counts()

    # Keep only regions with enough data
    for id_value in class_id.index:
        if class_id[id_value] < 10:
            my_df_dataframe = my_df_dataframe.loc[~(my_df_dataframe[new_column_name] == id_value)]

    return my_df_dataframe


def get_filter_max(my_df_dataframe, column_name):
    return my_df_dataframe[column_name].mean() + 3 * my_df_dataframe[column_name].std()


def aberrant_data_filter(my_df_dataset, column_name, filter_min_number=np.nan, filter_max_number=np.nan):
    # Aberrant data filter
    if filter_max_number == np.nan:
        get_filter_max(my_df_dataset, column_name)
    for x in my_df_dataset.index:
        if my_df_dataset.loc[x, column_name] > filter_max_number:
            my_df_dataset.drop(x, inplace=True)
        elif filter_min_number != np.nan:
            if my_df_dataset.loc[x, column_name] < filter_min_number:
                my_df_dataset.drop(x, inplace=True)


def explore_extreme_values(my_df_dataset, column_name, filter_min_number=np.nan, filter_max_number=np.nan):
    if filter_max_number == np.nan:
        get_filter_max(my_df_dataset, column_name)

    print("VALEURS ABERRANTES ÉLEVÉES - SALARY_IN_USD")
    print(my_df_dataset.loc[my_df_dataset[column_name] >
                            (my_df_dataset.salary_in_usd.mean() + 3 * my_df_dataset[column_name].std())], "\n")
    if filter_min_number != np.nan:
        print("VALEURS ABERRANTES INFÉRIEURES - SALARY_IN_USD < 20k")
        print(my_df_dataset.loc[my_df_dataset[column_name] <= filter_min_number])


def set_numeric_variable_into_class(my_df_dataset, column_name, conditions, new_values):
    my_df_dataset[column_name] = np.select(conditions, new_values)
    return my_df_dataset


def data_cleaning(my_df_dataset):
    # Keep only full-time rows (remove PT, CT and FL)
    mods = my_df_dataset.loc[(my_df_dataset.employment_type == "FT")]

    # Drop 'salary', 'salary_currency' and 'employement_type'
    mods = mods.drop(colums_to_drop, axis=1)

    # aberrant_data_filter(mods, 'salary_in_usd')

    recategorize_from_dictionary(mods, job_dictionary, 'job_title', 'job_category')
    mods = recategorize_country_by_continent(mods, "company_location", "company_continent")
    mods = recategorize_country_by_continent(mods, "employee_residence", "employee_continent")

    # Change 'experience_level' to be ordinal
    mods = recategorize_from_dictionary(mods, experience_dictionary, 'experience_level', 'experience_level')
    mods_with_numeric_salary = mods.copy()

    # Group 'salary_in_usd' in intervals
    mods = set_numeric_variable_into_class(mods, 'salary_in_usd',
                                           set_six_categorizing_conditions(mods, 'salary_in_usd', 50000),
                                           salary_categorical_values)

    # Save modified data as mods.csv
    mods.to_csv("mods.csv", index=False)

    return mods, mods_with_numeric_salary

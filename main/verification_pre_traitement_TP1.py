import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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


# Set values used as labels for salary
salary_categorical_values = ["[0,50 000[", "[50 000, 100 000[", "[100 000, 150 000[", "[150 000, 200 000[",
                             "[200 000, 250 000[", "[250 000, 300 000[", ">300 000"]


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


def data_cleaning():
    # Read the salaries' data
    salaries = pd.read_csv("salaries.csv", header=0)

    categorical_exploration(salaries)
    makes_box_plot(salaries)
    plot_distribution_for_each_variable(salaries)

    # Keep only full-time rows (remove PT, CT and FL)
    mods = salaries.loc[(salaries.employment_type == "FT")]

    # Drop 'salary', 'salary_currency' and 'employement_type'
    mods = mods.drop(colums_to_drop, axis=1)

    # aberrant_data_filter(mods, 'salary_in_usd')

    recategorize_from_dictionary(mods, job_dictionary, 'job_title', 'job_category')
    mods = recategorize_country_by_continent(mods, "company_location", "company_continent")
    mods = recategorize_country_by_continent(mods, "employee_residence", "employee_continent")

    # Group 'salary_in_usd' in intervals
    mods = set_salary_into_class(mods,
                                 set_six_categorizing_conditions(mods, 'salary_in_usd', 50000),
                                 salary_categorical_values)

    # Change 'experience_level' to be ordinal
    mods = recategorize_from_dictionary(mods, experience_dictionary, 'experience_level', 'experience_level')

    # Save modified data as mods.csv
    mods.to_csv("mods.csv", index=False)

    return salary_categorical_values


def set_salary_into_class(my_df_dataset, conditions, new_values):
    my_df_dataset["salary_in_usd"] = np.select(conditions, new_values)
    return my_df_dataset


# Function to generate a boxplot for each column
def data_visualisation(my_full_dataset, salary_variable):
    # Get the list of columns
    column_list = my_full_dataset.columns

    for column_name in column_list:

        if column_name != salary_variable:
            # Get the data of the column
            column_data = my_full_dataset[column_name].values

            # Get a boxplot comparing the target variable and every column
            fig = px.box(my_full_dataset, y=salary_variable, x=column_data
                         ).update_layout(
                yaxis_title="Salary in USD", xaxis_title=column_name,
                title="Distribution of " + salary_variable + " by " + column_name)
            fig.update_traces(orientation='v')  # Set boxes' orientation to target_variable(column_data)
            fig.write_image(column_name + ".svg")  # Save as scalable vector graphics


def categorical_exploration(my_df_dataset):
    column_list = my_df_dataset.columns

    print("CATEGORICAL VARIABLES FREQUENCY")
    for column_name in column_list:

        column_data = my_df_dataset[column_name].values

        if column_data.dtype == object or (column_data.dtype == np.int64 and np.unique(column_data).size < 5):
            print(column_name)
            print(my_df_dataset[column_name].value_counts(dropna=False))
            print("number of categories for " + column_name + " = ", len(my_df_dataset[column_name].unique()))
            print()


def makes_box_plot(my_df_dataset):
    column_list = my_df_dataset.columns
    for column_name in column_list:

        column_data = my_df_dataset[column_name].values

        if column_data.dtype != object and ((column_data.dtype == np.int64 and np.unique(column_data).size > 5) or
                                            column_data.dtype == np.float64):
            sns.boxplot(data=my_df_dataset[column_name])
            plt.ticklabel_format(style='plain', axis='y')
            plt.title("Distribution of " + column_name)
            plt.show()


def plot_distribution_for_each_variable(my_df_dataset):
    column_list = my_df_dataset.columns
    for column_name in column_list:

        column_data = my_df_dataset[column_name].values

        if column_data.dtype == object or (column_data.dtype == np.int64 and np.unique(column_data).size < 5):

            data = my_df_dataset[column_name].apply(str)
            data_to_plot = data.value_counts()

            plt.barh(width=data_to_plot.values, y=data_to_plot.index, data=data_to_plot)
            plt.title("Effectives of " + column_name + " variable")
            plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
            plt.yticks(data_to_plot.index)
            plt.xlabel('Effectives')
            plt.tight_layout()
            plt.gca().invert_yaxis()

            if len(data_to_plot.index) > 10:
                plt.yticks(fontsize=4)
            else:
                for i, v in enumerate(data_to_plot.values):
                    plt.text(v + 0.25, i, str(v), color='black', fontweight='bold')
            plt.show()

        if column_data.dtype != object and ((column_data.dtype == np.int64 and np.unique(column_data).size > 5) or
                                            column_data.dtype == np.float64):
            sns.histplot(my_df_dataset[column_name])
            plt.title("Distribution of " + column_name + " variable")
            plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
            plt.tight_layout()

            plt.show()

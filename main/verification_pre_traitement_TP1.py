import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


def data_cleaning():
    # Read the salaries' data
    salaries = pd.read_csv("salaries.csv", header=0)

    categorical_exploration(salaries)
    makes_box_plot(salaries)
    plot_distribution_for_each_variable(salaries)

    # Look at the first rows
    pd.set_option('display.max_columns', None)
    # Drop 'salary' and 'salary_currency'
    mods = salaries.drop(["salary", "salary_currency"], axis=1)

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
    mods['job_category'] = mods['job_title'].map(job_dictionary)

    # Change the company and employee locations for continents
    # Load data set with ISO codes and continents
    countries = pd.read_csv("country_file.csv", header=0)
    # Keep only the relevant columns from 'salaries.csv'
    countries = countries[["alpha-2", "region"]]
    # Add new column with regions
    countries = countries.rename(
        columns={"alpha-2": "company_location", "region": "company_continent"})  # Rename to uniformize datasets
    mods = pd.merge(mods, countries, on="company_location", how="inner")
    countries = countries.rename(columns={"company_location": "employee_residence",
                                          "company_continent": "employee_continent"})  # Rename to uniformize datasets
    mods = pd.merge(mods, countries, on="employee_residence", how="inner")

    # # Aberrant data filter
    # filter_max = (mods.salary_in_usd.mean() + 3*mods.salary_in_usd.std())
    # for x in mods.index:
    #     if mods.loc[x, 'salary_in_usd'] > filter_max:
    #         mods.drop(x, inplace=True)
    #     elif mods.loc[x, 'salary_in_usd'] < 20000:
    #         mods.drop(x, inplace=True)
    # mods.drop_duplicates(inplace=True)

    # Keep only full-time rows (remove PT, CT and FL)
    mods = mods.loc[(mods.employment_type == "FT")]
    print(mods['employment_type'].value_counts())

    # Drop replaced columns
    mods.drop(columns='employment_type', inplace=True)
    mods.drop(columns='employee_residence', inplace=True)
    mods.drop(columns='company_location', inplace=True)
    mods.drop(columns='job_title', inplace=True)

    # Keep only regions with enough data
    mods = mods.loc[(mods.employee_continent == "Americas") |
                    (mods.employee_continent == "Europe") |
                    (mods.employee_continent == "Asia")]

    mods = mods.loc[(mods.company_continent == "Americas") |
                    (mods.company_continent == "Europe") |
                    (mods.company_continent == "Asia")]
    
    # Change 'experience_level' to be ordinal
    mods["experience_level"] = mods['experience_level'].map({"EN": "1-EN", "MI": "2-MI", "SE": "3-SE", "EX": "4-EX"})

    # Save a copy of the cleaned dataset with the full salaries 
    mods.to_csv("cleaned_df_full_salaries.csv", index=False)
    # Group 'salary_in_usd' in intervals
    # Set conditions
    conditions = [
        (mods['salary_in_usd'] < 50000),
        (mods['salary_in_usd'] >= 50000) & (mods['salary_in_usd'] < 100000),
        (mods['salary_in_usd'] >= 100000) & (mods['salary_in_usd'] < 150000),
        (mods['salary_in_usd'] >= 150000) & (mods['salary_in_usd'] < 200000),
        (mods['salary_in_usd'] >= 200000) & (mods['salary_in_usd'] < 250000),
        (mods['salary_in_usd'] >= 250000) & (mods['salary_in_usd'] < 300000),
        (mods['salary_in_usd'] >= 300000)
    ]
    # Set values used as labels
    values = ["[0,50 000[", "[50 000, 100 000[", "[100 000, 150 000[", "[150 000, 200 000[", "[200 000, 250 000[",
              "[250 000, 300 000[", ">300 000"]
    mods["salary_in_usd"] = np.select(conditions, values)

    
    # Save modified data as mods.csv
    mods.to_csv("mods.csv", index=False)
    return values


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
            fig.update_xaxes(categoryorder='category ascending') # sort alphabetically
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

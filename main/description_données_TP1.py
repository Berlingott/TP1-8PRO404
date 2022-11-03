import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the salaries' data
salaries = pd.read_csv("./../salaries.csv", header=0)

# Display the five first lines
pd.set_option('display.max_columns', None)  # To display all columns
print(salaries.head())  # Print first 5 rows
print()

# Get column names
print("VARIABLES")
for column in salaries.columns:
    print(column)
print()

# Return tuple with dimensionality of the dataframe
print("DIMENSIONS DU DATAFRAME")
print(salaries.shape, "\n")

# Return a series with the data type of each column
print("TYPES DE VARIABLES")
print(salaries.dtypes, "\n")

# Print information about the dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info(), "\n")

# Count the number of instances
print("NOMBRE D'INSTANCES")
index = salaries.index
print(len(index), "\n")  # 946 instances

# Get min and max values for each numeric column
print("MIN-MAX")
print("work_year")
print(salaries["work_year"].min(), salaries["work_year"].max())  # 2020, 2022
print("salary")
print(salaries["salary"].min(), salaries["salary"].max())  # 2324, 30400000
print("salary_in_usd")
print(salaries["salary_in_usd"].min(), salaries["salary_in_usd"].max())  # 2324, 600000
print("remote_ratio")
print(salaries["remote_ratio"].min(), salaries["remote_ratio"].max(), "\n")  # 0, 100

# Print descriptive statistics
print("SALARIES.DESCRIBE()")
print(salaries.describe(), "\n")

# Print summary statistics for dataset and import to Excel
salaries.describe().to_excel("../statistic_description_salaries.xlsx")
# Count the total number of NaN per column
print("VALEURS NULLES PAR COLONNE")
print(salaries.isnull().sum(), "\n")

# Explore the categorical data
print("VARIABLES CATÉGORIELLES")
print(salaries['work_year'].value_counts(dropna=False), "\n")
print(salaries['experience_level'].value_counts(dropna=False), "\n")
print(salaries['employment_type'].value_counts(dropna=False), "\n")
print(salaries['job_title'].value_counts(dropna=False), "\n")
print(salaries['salary_currency'].value_counts(dropna=False), "\n")
print(salaries['employee_residence'].value_counts(dropna=False), "\n")
print(salaries['remote_ratio'].value_counts(dropna=False), "\n")
print(salaries['company_location'].value_counts(dropna=False), "\n")
print(salaries['company_size'].value_counts(dropna=False), "\n")

# Create a dataframe with all the duplicated variables
df_duplicates = salaries[salaries.duplicated()]

# Print the number of duplicates
print("NOMBRES DE DOUBLONS")
print(df_duplicates.shape, "\n")

# Print duplicates
print("APERÇU DES DOUBLONS")
print(df_duplicates, "\n")

# Extreme values
sns.boxplot(data=salaries['salary'])

# Set the y axis' values as non-exponential
plt.ticklabel_format(style='plain', axis='y')
plt.show()

sns.boxplot(data=salaries['salary_in_usd'])

# Set y axis' values as non-exponential
plt.ticklabel_format(style='plain', axis='y')
plt.show()

print("VALEURS ABERRANTES ÉLEVÉES - SALARY_IN_USD")
print(salaries.loc[salaries.salary_in_usd > (salaries.salary_in_usd.mean() + 3 * salaries.salary_in_usd.std())], "\n")
print("VALEURS ABERRANTES INFÉRIEURES - SALARY_IN_USD < 20k")
print(salaries.loc[
          salaries.salary_in_usd <= 20000])  # (0 or (salaries.salary_in_usd.mean() - 3*salaries.salary_in_usd.std()))])
# Note: of all the entries with will than 20K, none of them are US residents...

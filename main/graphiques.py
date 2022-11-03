from __init__ import *
from description_données_TP1 import *

salaries = pd.read_excel("../mods.xlsx", header=0)
pd.set_option('display.max_columns', None)
print(salaries.head())

# Tables per continent
americas = salaries.loc[(salaries.employee_continent == "Americas")]
europe = salaries.loc[(salaries.employee_continent == "Europe")]
asia = salaries.loc[(salaries.employee_continent == "Asia")]

# Information on the dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info(), "\n")

# Create a grouped boxplot
# make_boxplot_with_hue('job_category', 'salary_in_usd', 'company_continent', 'TEST TILE', salaries)
# make_boxplot_without_hue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
# make_bar_without_hue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
# make_bar_with_hue('job_category', 'salary_in_usd', 'company_continent', 'TEST TILE', salaries)
# make_facet_boxplot('job_category', 'salary_in_usd', 'TEST TILE', NA, EU, Asia)
# pie_graph('job_category', 'TEST TILE', salaries)
# make_table_describe_with_salary('job_category', salaries)
# calculate_khi2('job_category', 'salary_in_usd', salaries)

data = salaries["salary_in_usd"]
print(shapiro(data))  # ShapiroResult(statistic=0.980989933013916, p_value=6.602242641484679e-10)
make_corr_test_with_spearman_between_two_int('remote_ratio', 'salary_in_usd', salaries, "Correlation Test")
make_corr_test_with_spearman_with_one_string_and_one_int('job_category', 'salary_in_usd', salaries, "Correlation Test")

from __init__ import *
from description_données_TP1 import *

salaries = pd.read_excel("../mods.xlsx", header=0)
pd.set_option('display.max_columns', None)
print(salaries.head())

# Tableaux par continent
NA = salaries.loc[(salaries.employee_continent == "North America")]
EU = salaries.loc[(salaries.employee_continent == "Europe")]
Asia = salaries.loc[(salaries.employee_continent == "Asia")]

# informations sur le dataframe
print("INFORMATIONS SUR LE DATAFRAME")
print(salaries.info())
print()

# create grouped boxplot
#MakeBoxPlotWithHue('job_category', 'salary_in_usd', 'company_continent', 'TEST TILE', salaries)
#MakeBoxPlotWithoutHue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
#MakeBarWithoutHue('job_category', 'salary_in_usd', 'TEST TILE', salaries)
#MakeBarWithHue('job_category', 'salary_in_usd', 'company_continent', 'TEST TILE', salaries)
#makefacetboxplot('job_category', 'salary_in_usd', 'TEST TILE', NA, EU, Asia)
#piegraph('job_category', 'TEST TILE', salaries)
#MakeTableDescribeWithSalary('job_category', salaries)
#MakeKhi2Calcul('job_category', 'salary_in_usd', salaries)
data = salaries["salary_in_usd"]
print(shapiro(data))  #ShapiroResult(statistic=0.980989933013916, pvalue=6.602242641484679e-10)
make_corr_test_with_spearman_between_two_int('remote_ratio', 'salary_in_usd', salaries, "Correlation Test")
make_corr_test_with_spearman_with_one_string_and_one_int('job_category', 'salary_in_usd', salaries, "Correlation Test")

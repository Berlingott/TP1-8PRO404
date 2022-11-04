import pandas as pd
from utilExploreDataset import exploreDataset
from utilPlotGraphics import plotGraphics
from utilStatistics import performStatistics
from utilCleanDataset import cleanDataset

########################################################################################################################
#                                               USER PARAMETERS                                                        #
########################################################################################################################

# Define the pathname of the datset
dataset_pathname = "salaries.csv"

# Define the target variable
target_variable = "salary_in_usd"

# Define the ratio of NaN
max_NaN_ratio = 0.1

########################################################################################################################
#                                                   LOAD THE DATASET                                                   #
########################################################################################################################

# Load the data
my_df_dataset = pd.read_csv(dataset_pathname, sep=",", header=0)

print()
print("----------------- ORIGINAL DATA -------------------------")
print()

# to print all the columns de-comment next line
# pd.set_option('display.max_columns', None)

# Print some instances
print(my_df_dataset.head())
print(my_df_dataset.describe())

########################################################################################################################
#                                            GET INFORMATION ON THE DATASET                                            #
########################################################################################################################

# exploration of the dataset before cleaning

# Print the shape information of the dataset
exploreDataset.compute_instance_and_variable_number(my_df_dataset)
# Print information for each variable
exploreDataset.get_variable_information(my_df_dataset)
# plot distribution for each variable
exploreDataset.makes_box_plot(my_df_dataset)
exploreDataset.plot_distribution_for_each_variable(my_df_dataset)

# de-comment to explore de details of the extremes values of the target variable
# verification_pre_traitement_TP1.explore_extreme_values(my_df_dataset, target_variable, 20000)

# cleaning the dataset
my_df_dataset, my_full_dataset = cleanDataset.data_cleaning(my_df_dataset)
class_id = cleanDataset.salary_categorical_values

print()
print("----------------- CLEANED DATA -------------------------")

# Print the shape information of the cleaned dataset
exploreDataset.compute_instance_and_variable_number(my_df_dataset)

# Print information for each cleaned variable
exploreDataset.get_variable_information(my_df_dataset)

# Print information on the cleaned target variable
exploreDataset.get_target_variable_information(my_df_dataset, target_variable, class_id)

# plot distribution for each variable
exploreDataset.makes_box_plot(my_df_dataset)
exploreDataset.plot_distribution_for_each_variable(my_df_dataset)

########################################################################################################################
#                                                    PLOT GRAPHICS                                                     #
########################################################################################################################

# Print box plot for target_variable depending on column data
plotGraphics.data_visualisation(my_full_dataset, target_variable)

# Plot all graphics
plotGraphics.generate_all_plots(class_id, my_df_dataset, target_variable)

# Plot each variable vs. each variable for numerical values
attribute_list = plotGraphics.plot_all_scatter_graphics(class_id, my_df_dataset, target_variable)

########################################################################################################################
#                                                      STATISTICS                                                      #
########################################################################################################################

# Compute the matrix of correlations between each numerical variable
# because we have no numerical value in the cleaned dataset, this fonction is silent
# performStatistics.correlation_person_matrix(attribute_list, my_df_dataset)

# Perform the ANOVA test for all variable that can be plotted with box plot
# For this project, this function will print nothing because of absence of numeric variables
performStatistics.anova_for_all(class_id, my_df_dataset, target_variable)

# Perform the independent test for all variable that can be plotted with bar plot
performStatistics.independent_test_for_all(class_id, my_df_dataset, target_variable)

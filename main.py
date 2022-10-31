import numpy as np
import pandas as pd

from utilCleanDataset import cleanDataset
from utilPlotGraphics import plotGraphics
from utilStatistics import performStatistics
from main import verification_pre_traitement_TP1


########################################################################################################################
#                                               USER PARAMETERS                                                        #
########################################################################################################################

#Call the data cleaning method
verification_pre_traitement_TP1.DataCleaning()

# Define the pathname of the datset
dataset_pathname = "mods.csv"

# Define the target variable
target_variable = "salary_in_usd"

# Define the ratio of NaN
max_NaN_ratio = 0.1

########################################################################################################################
#                                                   LOAD THE DATASET                                                   #
########################################################################################################################

# Load the data
my_df_dataset = pd.read_csv(dataset_pathname, sep=",", header=0)

# Print some instances
print(my_df_dataset.head())

########################################################################################################################
#                                            GET INFORMATION ON THE DATASET                                            #
########################################################################################################################

# Print the shape information of the dataset
cleanDataset.compute_instance_and_variable_number(my_df_dataset)

# Print information for each variable
cleanDataset.get_varaible_information(my_df_dataset)

# Print information on the target variable
# class_id = cleanDataset.get_target_variable_information(my_df_dataset, target_variable)
class_id = verification_pre_traitement_TP1.DataCleaning()

# Print box plot for target_variable depending on column data
# verification_pre_traitement_TP1.dataVisualisation(my_df_dataset, target_variable)

########################################################################################################################
#                                                    PLOT GRAPHICS                                                     #
########################################################################################################################

# Plot all graphics
plotGraphics.plot_all_plots(class_id, my_df_dataset, target_variable)

# Plot each variable vs. each variable for numerical values
attribute_list = plotGraphics.plot_all_scatter_graphics(class_id, my_df_dataset, target_variable)

########################################################################################################################
#                                                      STATISTICS                                                      #
########################################################################################################################

# Compute the matrix of correlations between each numerical variable
performStatistics.correlation_person_matrix(attribute_list, my_df_dataset)

# Perform the ANOVA test for all variable that can be plot with box plot
performStatistics.anova_for_all(class_id, my_df_dataset, target_variable)

# Perform the independant test for all variable that can be plot with bar plot
performStatistics.independent_test_for_all(class_id, my_df_dataset, target_variable)







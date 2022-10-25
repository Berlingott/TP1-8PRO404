import numpy as np
import pandas as pd

from scipy.stats import shapiro, levene, f_oneway, kruskal, chi2_contingency, pearsonr

def anova_for_all(class_id, my_df_dataset, target_variable):

    # Get the list of columns
    column_list = my_df_dataset.columns

    for column_name in column_list:

        if column_name != target_variable:

            # Get the data of the column
            column_data = my_df_dataset[column_name].values
            # Get all possible values of the column
            feature_values = np.unique(column_data)

            if column_data.dtype != object and feature_values.size > 5:

                print("\n")
                print("- " + column_name)

                column_data_list = []

                for id_value in class_id:
                    # Get the indices of instances belonging to the class "id_value"
                    indices = np.where(my_df_dataset[target_variable] == id_value)
                    # Get all values of all identified instances
                    column_data_list.append(my_df_dataset[column_name].values[indices])

                # Test the data for the normality assumption
                normality_count = 0

                for j in range(len(class_id)):

                    if(len(column_data_list[j]) > 3):
                        # Perform the shapiro test
                        stat, pval = shapiro(column_data_list[j])

                        if pval > 0.05:
                            normality_count = normality_count + 1

                # Test of homogeneity of variances
                if len(class_id) == 2:

                    fval, pval = levene(column_data_list[0], column_data_list[1])

                elif len(class_id) == 3:

                    fval, pval = levene(column_data_list[0], column_data_list[1], column_data_list[2])

                elif len(class_id) == 4:

                    fval, pval = levene(column_data_list[0], column_data_list[1], column_data_list[2],
                                        column_data_list[3])

                # Test of ANOVA
                if (normality_count == len(class_id)) and (pval > 0.05):

                    print("-    normality count: " + str(normality_count))
                    print("-    pval (homogeneity of variances): " + str(pval))

                    if len(class_id) == 2:

                        fval, pval = f_oneway(column_data_list[0], column_data_list[1])

                    elif len(class_id) == 3:

                        fval, pval = f_oneway(column_data_list[0], column_data_list[1], column_data_list[2])

                    elif len(class_id) == 4:

                        fval, pval = f_oneway(column_data_list[0], column_data_list[1], column_data_list[2],
                                              column_data_list[4])

                    print("     - The null hypothesis is that there is any difference in the '" + column_name +
                          "' variable between group of people according to '" + target_variable + ".")
                    print("     - pvalue: ", pval)

                    if pval < 0.05:

                        print("     - we reject the null hypothesis")

                    else:

                        print("     - we accept the null hypothesis")

                else:

                    print("     - normality count: " + str(normality_count))
                    print("     - pval (homogeneity of variances): " + str(pval))
                    print("     - The assumptions are not satisfied")

                    print(" We proceed to a non-parametric version of ANOVA : Kruskal-Wallis H-test")

                    if len(class_id) == 2:

                        fval, pval = kruskal(column_data_list[0], column_data_list[1])

                    elif len(class_id) == 3:

                        fval, pval = kruskal(column_data_list[0], column_data_list[1], column_data_list[2])

                    elif len(class_id) == 4:

                        fval, pval = kruskal(column_data_list[0], column_data_list[1], column_data_list[2],
                                             column_data_list[4])

                    print("     - The null hypothesis is that there is any difference in the '" + column_name +
                          "' variable between group of people according to '" + target_variable + ".")
                    print("     - pvalue: ", pval)

                    if pval < 0.05:

                        print("     - we reject the null hypothesis")

                    else:

                        print("     - we accept the null hypothesis")


def independent_test_for_all(class_id, my_df_dataset, target_variable):

    # Get the list of columns
    column_list = my_df_dataset.columns

    for column_name in column_list:

        if column_name != target_variable:

            # Get the data of the column
            column_data = my_df_dataset[column_name].values
            # Get all possible values of the column
            feature_values = np.unique(column_data)

            if (column_data.dtype == object) or (column_data.dtype != object and feature_values.size <= 5):

                print("\n")
                print("- " + column_name)

                obs = []

                column_value = np.unique(column_data)

                for id_value in class_id:

                    # Get the indices of instances belonging to the class "id_value"
                    indices = np.where(my_df_dataset[target_variable] == id_value)[0]
                    # Get all values of all identified instances
                    tmp_column_data = my_df_dataset[column_name].values[indices]

                    tmp_obs = []

                    for value in column_value:

                        indices = np.where(tmp_column_data == value)[0]
                        tmp_obs.append(indices.size)

                    obs.append(np.array(tmp_obs))

                results = chi2_contingency(np.array(obs))

                print("     The chi2 is:")
                print("     - " + str(results[0]) + " with a p-value of " + str(results[1]))

                if results[1] < 0.05:

                    print("         - There is a dependency between variables")

                else:

                    print("         - There is no dependency between variables")

                print("     Observed distribution")
                print(np.array(obs))
                print("     Expected distribution")
                print(results[3])


def correlation_person_matrix(attribute_list, my_df_dataset):

    correlation_coefficient_matrix = np.zeros((len(attribute_list), len(attribute_list)))
    pvalue_matrix = np.zeros((len(attribute_list), len(attribute_list)))

    for i in range(len(attribute_list)):

        for j in range(len(attribute_list)):

            if i>=j:


                x = my_df_dataset[attribute_list[i]].values
                y = my_df_dataset[attribute_list[j]].values

                r1, pvalue = pearsonr(x, y)

                if i == j:

                    correlation_coefficient_matrix[i, j] = r1
                    pvalue_matrix[i, j] = pvalue

                if i>j:
                    correlation_coefficient_matrix[i, j] = r1
                    pvalue_matrix[i, j] = pvalue

                    correlation_coefficient_matrix[j, i] = r1
                    pvalue_matrix[j, i] = pvalue

    print("\n\n")
    print("This is the correlation matrix between variables and its p_value matrix. The variable are: ")
    print(attribute_list)
    print("\n")
    print(correlation_coefficient_matrix)
    print("\n")
    print(pvalue_matrix)



















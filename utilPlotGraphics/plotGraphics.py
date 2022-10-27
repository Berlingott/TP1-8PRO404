import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def plot_all_plots(class_id, my_df_dataset, target_variable):

    # Get the list of columns
    column_list = my_df_dataset.columns

    for column_name in column_list:

        if column_name != target_variable:

            # Get the data of the column
            column_data = my_df_dataset[column_name].values

            # Get all possible values of the column
            feature_values = np.unique(column_data)

            if column_data.dtype == object or (column_data.dtype != object) & (feature_values.size <= 5):
                plot_bar_plots(class_id, my_df_dataset, column_name, target_variable)






def plot_bar_plots(class_id, my_df_dataset, column_name, target_variable):

    my_width = 1/len(class_id)

    counter = 0
    # add distinctive colors
    col_counter = 0
    color_list = ["red", "lime", "aqua", "navy", "silver", "darkorange", "purple", "darkgreen", "yellow",
                      "fuchsia", "saddlebrown"]
    feature_value = np.unique(my_df_dataset[column_name])

    print("\n\n")
    print("Bar plot of " + column_name)

    for id_value in class_id:

        # Get the indices of instances belonging to the class "id_value"
        indices = np.where(my_df_dataset[target_variable] == id_value)
        # Get all values of all identified instances
        column_data = my_df_dataset[column_name].values[indices]

        # Initialize two empty list
        tmp_instance_number = []
        tmp_percentages = []

        print("     - class: " + str(id_value))
        print("         " + str(feature_value))

        for value in feature_value:

            tmp_indices = np.where(column_data == value)
            tmp_instance_number.append(tmp_indices[0].size)
            tmp_percentages.append((tmp_indices[0].size / indices[0].size) * 100)

        print("         Instance number: " + str(tmp_instance_number))
        print("         Percentages: " + str(tmp_percentages))

        # Create the data label for the bar plot
        data_label = target_variable + ": " + str(id_value)
        # Compute the number of bars
        X = np.arange(len(tmp_percentages)) * 2

        plt.bar((X - counter+(len(class_id)/10)) + counter*my_width + (my_width/2), tmp_percentages, width=my_width, alpha=0.7,
                label=data_label, edgecolor="k", color=color_list[col_counter])
        counter = counter + 0.2
        col_counter = col_counter + 1   # switch to next color for next class id

    plt.title(target_variable + " by " + column_name, fontsize=10)
    plt.xticks(np.arange(feature_value.size)*2, feature_value, rotation=90)
    plt.ylabel("Percentage of people")
    plt.xlabel(column_name)
    plt.legend(["[0,50 000[", "[50 000, 100 000[", "[100 000, 150 000[", "[150 000, 200 000[", "[200 000, 250 000[", "[250 000, 300 000[", ">300 000"], #reorder legend labels
        bbox_to_anchor=(1.04, 1), loc="upper left", prop = {"size" : 6})    # position and resize legend
    plt.tight_layout()
    plt.figure(figsize=(35, 25))
    plt.show()


def filter_column_for_scatter_plots(my_df_dataset):

    column_list = my_df_dataset.columns
    new_column_list = []

    for column_name in column_list:

        column_data = my_df_dataset[column_name].values

        feature_values = np.unique(column_data)

        if column_data.dtype != object and feature_values.size > 5:
            new_column_list.append(column_name)

    return new_column_list


def plot_scatter_graphics(column_name_1, column_name_2, class_id, my_df_dataset, target_variable):

    # Initialization
    column_names = [column_name_1, column_name_2]
    color_list = ["r", "g", "k", "b", "y", "m", "c"]
    marker_list = ["o", "s", "*", "v", "<", "1", "8", "p"]
    counter = 0
    data_labels = []

    for id_value in class_id:

        column_data = []
        indices = np.where(my_df_dataset[target_variable] == id_value)[0]

        for column_name in column_names:

            column_data.append(my_df_dataset[column_name].values[indices])

        data_label = target_variable + " " + str(id_value)
        data_labels.append(data_label)


        plt.scatter(column_data[0], column_data[1], marker=marker_list[counter], c=color_list[counter],
                    alpha=0.5, edgecolors="k", label=data_label)

        counter = counter + 1

    plt.title(column_names[0] + " vs. " + column_names[1], fontsize=20)
    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.legend(data_labels)
    plt.show()













def plot_all_scatter_graphics(class_id, my_df_dataset, target_variable):

    attribute_list = filter_column_for_scatter_plots(my_df_dataset)

    for i in range(len(attribute_list)):

        for j in range(len(attribute_list)):

            if i<j:

                plot_scatter_graphics(attribute_list[i], attribute_list[j], class_id, my_df_dataset, target_variable)

    return attribute_list












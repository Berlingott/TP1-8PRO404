import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compute_instance_and_variable_number(my_df_dataset):

    # Get the numpy array from the dataframe
    my_data = my_df_dataset.values

    # Get the shape of the data
    data_shape = my_data.shape

    # Print the information
    print("\nThere are " + str(data_shape[0]) + " instances and " + str(data_shape[1]) + " variables.")


def get_variable_information(my_df_dataset):
    for column_name in my_df_dataset.columns:
        print()
        print("- " + column_name)

        column_data = my_df_dataset[column_name].values

        if column_data.dtype != object and ((column_data.dtype == np.int64 and np.unique(column_data).size > 5) or
                                            column_data.dtype == np.float64):

            try:

                min_value = np.min(column_data)
                max_value = np.max(column_data)
                nan_presence = np.sum(np.isnan(column_data))

            except TypeError:

                min_value = "Error"
                max_value = "Error"
                nan_presence = "Error"

            print("     the minimum value is " + str(min_value) + " and the maximum value is " + str(max_value) + ".")
            print("         there are NaN value: " + str(nan_presence))

        else:

            try:

                unique_values = np.unique(column_data[~pd.isnull(column_data)])
                nan_presence = np.sum(pd.isnull(column_data))

            except TypeError:

                unique_values = "Error"
                nan_presence = "Error"

            print("     the values and their frequencies are: ")
            print(my_df_dataset[column_name].value_counts(dropna=True))
            print("         there are NaN value: " + str(nan_presence))
            print("         there are ", len(my_df_dataset[column_name].unique()),
                  " classes for " + column_name + " variable")


def get_target_variable_information(my_df_dataset, target_variable, class_id):

    print("\nInformation on the '" + target_variable + "' column:")

    for id_value in class_id:

        indices = np.where(my_df_dataset[target_variable] == id_value)
        print("     - " + str(id_value) + " with " + str(indices[0].size) + " instances")

    return class_id



def categorical_exploration(my_df_dataset):
    column_list = my_df_dataset.columns

    print("CATEGORICAL VARIABLES FREQUENCY")
    for column_name in column_list:

        column_data = my_df_dataset[column_name].values

        if column_data.dtype == object or (column_data.dtype == np.int64 and np.unique(column_data).size < 5):
            print(column_name)
            print(my_df_dataset[column_name].value_counts(dropna=True))
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













import numpy as np
import pandas as pd


def compute_instance_and_variable_number(my_df_dataset):

    # Get the numpy array from the dataframe
    my_data = my_df_dataset.values

    # Get the shape of the data
    data_shape = my_data.shape

    # Print the information
    print("\nThere are " + str(data_shape[0]) + " instances and " + str(data_shape[1]) + " variables.")


def get_varaible_information(my_df_dataset):

    for column_name in my_df_dataset.columns:

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

            print("     the values are:" + str(list(unique_values)))
            print("         there are NaN value: " + str(nan_presence))


def get_target_variable_information(my_df_dataset, target_variable):

    class_id = np.unique(my_df_dataset[target_variable])

    print("\nInformation on the '" + target_variable + "' column:")

    for id_value in class_id:

        indices = np.where(my_df_dataset[target_variable] == id_value)
        print("     - " + str(id_value) + " with " + str(indices[0].size) + " instances")

    return class_id
















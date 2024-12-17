import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error



############################### Calculate statistical measures for all LGAs at MB level  ###############################

df = pd.read_excel('MB_Integrated_Dataset_Unfiltered_Veg.xlsx')

def calculate_mad(dataset):
    """
    Calculate the Mean Absolute Deviation from 0 of a dataset.
    Parameters:
    - dataset (list or numpy array): The dataset to calculate MAD for.
    Returns:
    - float: The MAD of the dataset from 0.
    """
    mad = np.mean(np.abs(dataset))
    return mad

metric_matrix = np.empty((1+6+6, 33), dtype=object)
metric_matrix[:] = np.nan

unique_lgas = df['HEAT - LGA'].unique()
num = 0
for lga in unique_lgas:
    df_unique = df[df['HEAT - LGA'] == lga]
    print(lga)
    np_unique = np.asarray(df_unique)
    prioritarian_expected_tree_area = np.empty((df_unique.shape[0], 1), dtype=object)
    prioritarian_expected_tree_area[:] = np.nan
    egalitarian_expected_tree_area = np.empty((df_unique.shape[0], 1), dtype=object)
    egalitarian_expected_tree_area[:] = np.nan
    sufficientarian_expected_tree_area = np.empty((df_unique.shape[0], 1), dtype=object)
    sufficientarian_expected_tree_area[:] = np.nan


    more_trees_sqm = sum(np_unique[:, 14]) - sum(np_unique[:, 42])
    print(more_trees_sqm)


    ########## Prioritarian #############

    prio_weights = 0
    for i in range(np_unique.shape[0]):
        prio_weights += np_unique[i, 3] - np_unique[i, 42]
    print(prio_weights)

    for i in range(prioritarian_expected_tree_area.shape[0]):
        prioritarian_expected_tree_area[i, 0] = np_unique[i, 42] + more_trees_sqm * (
                    np_unique[i, 3] - np_unique[i, 42]) / prio_weights

    List_limited_veg_area = []
    additional_trees = 1
    while additional_trees != 0:
        additional_trees = 0
        prio_weights = 0
        for i in range(prioritarian_expected_tree_area.shape[0]):
            if prioritarian_expected_tree_area[i, 0] > np_unique[i, 43]:
                List_limited_veg_area.append(i)
                additional_trees += prioritarian_expected_tree_area[i, 0] - np_unique[i, 43]
                prioritarian_expected_tree_area[i, 0] = np_unique[i, 43]

        for i in range(np_unique.shape[0]):
            if i not in List_limited_veg_area:
                prio_weights += np_unique[i, 3] - prioritarian_expected_tree_area[i, 0]

        for i in range(prioritarian_expected_tree_area.shape[0]):
            if i not in List_limited_veg_area:
                prioritarian_expected_tree_area[i, 0] += additional_trees * (
                            np_unique[i, 3] - prioritarian_expected_tree_area[i, 0]) / prio_weights

    df_unique['2022_prioritarian_expected_tree_area'] = prioritarian_expected_tree_area[:, 0]

    ########### Egalitarian #############
    egal_ratio_tree = more_trees_sqm / sum(np_unique[:, 3])
    # print(egal_ratio_tree)
    for i in range(egalitarian_expected_tree_area.shape[0]):
        egalitarian_expected_tree_area[i, 0] = np_unique[i, 42] + egal_ratio_tree * np_unique[i, 3]

    List_limited_veg_area = []
    additional_trees = 1
    total_available_area = sum(np_unique[:, 3])

    while additional_trees != 0:
        additional_trees = 0
        for i in range(egalitarian_expected_tree_area.shape[0]):
            if egalitarian_expected_tree_area[i, 0] > np_unique[i, 43]:
                List_limited_veg_area.append(i)
                additional_trees += egalitarian_expected_tree_area[i, 0] - np_unique[i, 43]
                total_available_area -= np_unique[i, 3]
                egalitarian_expected_tree_area[i, 0] = np_unique[i, 43]

        for i in range(egalitarian_expected_tree_area.shape[0]):
            if i not in List_limited_veg_area:
                egalitarian_expected_tree_area[i, 0] += additional_trees / total_available_area * np_unique[i, 3]

    df_unique['2022_egalitarian_expected_tree_area'] = egalitarian_expected_tree_area[:, 0]

    ########### Sufficientarian #############
    sufficientarian_percentage = np.empty((sufficientarian_expected_tree_area.shape[0], 1), dtype=object)
    sufficientarian_percentage[:] = np.nan

    for i in range(sufficientarian_expected_tree_area.shape[0]):
        sufficientarian_percentage[i, 0] = np_unique[i, 42] / np_unique[i, 3]

    count = 0
    while count < np_unique.shape[0]:
        # print(count)
        # print(more_trees_sqm)
        min_value = np.min(sufficientarian_percentage)
        min_indices = np.where(sufficientarian_percentage == min_value)[0]
        # print(min_indices)
        if more_trees_sqm < 1:
            break
        next_min_value = np.min(sufficientarian_percentage[sufficientarian_percentage > min_value])
        for i in range(len(min_indices)):
            allocation = (next_min_value - min_value) * np_unique[min_indices[i], 3]
            if allocation > more_trees_sqm:
                sufficientarian_percentage[min_indices[i], 0] = more_trees_sqm / np_unique[min_indices[i], 3] + min_value
                break
            more_trees_sqm -= allocation
            sufficientarian_percentage[min_indices[i], 0] = next_min_value
        count += 1

    for i in range(sufficientarian_expected_tree_area.shape[0]):
        sufficientarian_expected_tree_area[i, 0] = np_unique[i, 3] * sufficientarian_percentage[i, 0]

    additional_trees = 1
    List_limited_veg_area = []
    while additional_trees != 0:
        additional_trees = 0
        prio_weights = 0
        for i in range(sufficientarian_expected_tree_area.shape[0]):
            if sufficientarian_expected_tree_area[i, 0] > np_unique[i, 43]:
                List_limited_veg_area.append(i)
                additional_trees += sufficientarian_expected_tree_area[i, 0] - np_unique[i, 43]
                sufficientarian_expected_tree_area[i, 0] = np_unique[i, 43]

        sufficientarian_percentage = np.empty((sufficientarian_expected_tree_area.shape[0], 1), dtype=object)
        sufficientarian_percentage[:] = np.nan

        for i in range(sufficientarian_expected_tree_area.shape[0]):
            if i not in List_limited_veg_area:
                sufficientarian_percentage[i, 0] = sufficientarian_expected_tree_area[i, 0] / np_unique[i, 3]
            else:
                sufficientarian_percentage[i, 0] = 1

        count = 0
        while count < np_unique.shape[0]:
            print(count)
            print(additional_trees)
            min_value = np.min(sufficientarian_percentage)
            min_indices = np.where(sufficientarian_percentage == min_value)[0]
            # print(min_indices)
            try:
                next_min_value = np.min(sufficientarian_percentage[sufficientarian_percentage > min_value])
            except:
                break

            if additional_trees < 1:
                break
            for i in range(len(min_indices)):
                allocation = (next_min_value - min_value) * np_unique[min_indices[i], 3]
                if allocation > additional_trees:
                    sufficientarian_percentage[min_indices[i], 0] = additional_trees / np_unique[
                        min_indices[i], 3] + min_value
                    break
                additional_trees -= allocation
                sufficientarian_percentage[min_indices[i], 0] = next_min_value
            count += 1

        for i in range(sufficientarian_expected_tree_area.shape[0]):
            if i not in List_limited_veg_area:
                sufficientarian_expected_tree_area[i, 0] = np_unique[i, 3] * sufficientarian_percentage[i, 0]
    df_unique['2022_sufficientarian_expected_tree_area'] = sufficientarian_expected_tree_area[:, 0]

    #######################################




    df_unique['2022_prioritarian_expected_more_trees'] = (df_unique['2022_prioritarian_expected_tree_area'] - df_unique['2016 - AREA_TREE - modified again']) / df_unique['2022 - MMB_AREA'] * 10000
    df_unique['2022_egalitarian_expected_more_trees'] = (df_unique['2022_egalitarian_expected_tree_area'] - df_unique['2016 - AREA_TREE - modified again']) / df_unique['2022 - MMB_AREA'] * 10000
    df_unique['2022_sufficientarian_expected_more_trees'] = (df_unique['2022_sufficientarian_expected_tree_area'] - df_unique['2016 - AREA_TREE - modified again']) / df_unique['2022 - MMB_AREA'] * 10000

    df_unique['2022_prioritarian_difference'] = (df_unique['2022 - Actual - more AREA_TREE/Hec'] - df_unique['2022_prioritarian_expected_more_trees'])
    df_unique['2022_egalitarian_difference'] = (df_unique['2022 - Actual - more AREA_TREE/Hec'] - df_unique['2022_egalitarian_expected_more_trees'])
    df_unique['2022_sufficientarian_difference'] = (df_unique['2022 - Actual - more AREA_TREE/Hec'] - df_unique['2022_sufficientarian_expected_more_trees'])



    metric_matrix[0, num] = lga

    col_num = 1
    for column in ['2022_prioritarian_difference', '2022_egalitarian_difference', '2022_sufficientarian_difference']:
        df_unique[column] = df_unique[column] / 100
        dataset = df_unique[column]
        mad = calculate_mad(dataset)
        print(f"Mean Absolute Deviation from 0: {mad}")
        metric_matrix[col_num, num] = mad
        col_num += 1

    columns_to_scale = [
        '2022 - Actual - more AREA_TREE/Hec',
        '2022_prioritarian_expected_more_trees',
        '2022_egalitarian_expected_more_trees',
        '2022_sufficientarian_expected_more_trees'
    ]

    # Scale down the specified columns by 100
    for column in columns_to_scale:
        df_unique[column] = df_unique[column] / 100
    mse_prioritarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'], df_unique['2022_prioritarian_expected_more_trees'])
    mse_egalitarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'], df_unique['2022_egalitarian_expected_more_trees'])
    mse_sufficientarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'], df_unique['2022_sufficientarian_expected_more_trees'])


    rmse_prioritarian = np.sqrt(mse_prioritarian)
    metric_matrix[4, num] = rmse_prioritarian
    rmse_egalitarian = np.sqrt(mse_egalitarian)
    metric_matrix[5, num] = rmse_egalitarian
    rmse_sufficientarian = np.sqrt(mse_sufficientarian)
    metric_matrix[6, num] = rmse_sufficientarian

    print(f"RMSE - Prioritarian: {rmse_prioritarian}")
    print(f"RMSE - Egalitarian: {rmse_egalitarian}")
    print(f"RMSE - Sufficientarian: {rmse_sufficientarian}")

    num += 1







unique_lgas = df['HEAT - LGA'].unique()
num = 0
for lga in unique_lgas:
    df_unique = df[df['HEAT - LGA'] == lga]
    print(lga)

    col_num = 7
    for column in ['Prioritarian Difference', 'Egalitarian Difference',
                   'Sufficientarian Difference']:
        df_unique[column] = df_unique[column] / 100
        dataset = df_unique[column]
        mad = calculate_mad(dataset)
        print(f"Mean Absolute Deviation from 0: {mad}")
        metric_matrix[col_num, num] = mad
        col_num += 1

    columns_to_scale = [
        '2022 - Actual - more AREA_TREE/Hec',
        '2022 - Expected - Prioritarian - more AREA_TREE/Hec',
        '2022 - Expected - Egalitarian - more AREA_TREE/Hec',
        '2022 - Expected - Sufficientarian - more AREA_TREE/Hec'
    ]

    # Scale down the specified columns by 100
    for column in columns_to_scale:
        df_unique[column] = df_unique[column] / 100
    mse_prioritarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'],
                                          df_unique['2022 - Expected - Prioritarian - more AREA_TREE/Hec'])
    mse_egalitarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'],
                                         df_unique['2022 - Expected - Egalitarian - more AREA_TREE/Hec'])
    mse_sufficientarian = mean_squared_error(df_unique['2022 - Actual - more AREA_TREE/Hec'],
                                             df_unique['2022 - Expected - Sufficientarian - more AREA_TREE/Hec'])


    rmse_prioritarian = np.sqrt(mse_prioritarian)
    metric_matrix[10, num] = rmse_prioritarian
    rmse_egalitarian = np.sqrt(mse_egalitarian)
    metric_matrix[11, num] = rmse_egalitarian
    rmse_sufficientarian = np.sqrt(mse_sufficientarian)
    metric_matrix[12, num] = rmse_sufficientarian

    print(f"RMSE - Prioritarian: {rmse_prioritarian}")
    print(f"RMSE - Egalitarian: {rmse_egalitarian}")
    print(f"RMSE - Sufficientarian: {rmse_sufficientarian}")

    num += 1


Row_titles = ['LGA Name',
              'Independently_MAD_Prioritarian',
              'Independently_MAD_Egalitarian',
              'Independently_MAD_Sufficientarian',
              'Independently_RMSE_Prioritarian',
              'Independently_RMSE_Egalitarian',
              'Independently_RMSE_Sufficientarian',
              'InConjuction_MAD_Prioritarian',
              'InConjuction_MAD_Egalitarian',
              'InConjuction_MAD_Sufficientarian',
              'InConjuction_RMSE_Prioritarian',
              'InConjuction_RMSE_Egalitarian',
              'InConjuction_RMSE_Sufficientarian']

list_column = np.array(Row_titles).reshape(-1, 1)

# Concatenate the list as the first column of the array
metric_matrix_titled = np.hstack((list_column, metric_matrix))


df_pred = pd.DataFrame(metric_matrix_titled)
filepath_pred = 'Statistical_Measures_Actual_LGAs_MB_Veg.xlsx'
df_pred.to_excel(filepath_pred, index=False)

########################################################################################################################

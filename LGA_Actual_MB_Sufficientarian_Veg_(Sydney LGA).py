import numpy as np
import pandas as pd



################ Calculate tree areas based on sufficientarian theory of justice for LGAs independently  ###################
### First step ###
### Sample for Sydney LGA ###

# df = pd.read_excel('MB_Integrated_Dataset_Unfiltered_Veg.xlsx')
#
# sydney_rows = df[df['HEAT - LGA'] == 'Sydney']
# print(sydney_rows.shape)
# sydney_rows.to_excel('Sydney_LGA_MB_Integrated_Dataset_Unfiltered_Veg.xlsx', index=False)




########################################################################################################################
### Second step ###

LGA = pd.read_excel("Sydney_LGA_MB_Integrated_Dataset_Unfiltered_Veg.xlsx")
LGA = np.asarray(LGA)

sufficientarian_expected_tree_area = np.empty((LGA.shape[0], 1), dtype=object)
sufficientarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(LGA[:, 14]) - sum(LGA[:, 42])
print(more_trees_sqm)

sufficientarian_percentage = np.empty((sufficientarian_expected_tree_area.shape[0], 1), dtype=object)
sufficientarian_percentage[:] = np.nan

for i in range(sufficientarian_expected_tree_area.shape[0]):
    sufficientarian_percentage[i, 0] = LGA[i, 42] / LGA[i, 3]

count = 0
while count < LGA.shape[0]:
    print(count)
    print(more_trees_sqm)
    min_value = np.min(sufficientarian_percentage)
    min_indices = np.where(sufficientarian_percentage == min_value)[0]
    # print(min_indices)
    if more_trees_sqm < 1:
        break
    next_min_value = np.min(sufficientarian_percentage[sufficientarian_percentage > min_value])
    for i in range(len(min_indices)):
        allocation = (next_min_value - min_value) * LGA[min_indices[i], 3]
        if allocation > more_trees_sqm:
            sufficientarian_percentage[min_indices[i], 0] = more_trees_sqm / LGA[min_indices[i], 3] + min_value
            break
        more_trees_sqm -= allocation
        sufficientarian_percentage[min_indices[i], 0] = next_min_value
    count += 1

for i in range(sufficientarian_expected_tree_area.shape[0]):
    sufficientarian_expected_tree_area[i, 0] = LGA[i, 3] * sufficientarian_percentage[i, 0]



additional_trees = 1
List_limited_veg_area = []
while additional_trees != 0:
    additional_trees = 0
    prio_weights = 0
    for i in range(sufficientarian_expected_tree_area.shape[0]):
        if sufficientarian_expected_tree_area[i, 0] > LGA[i, 43]:
            List_limited_veg_area.append(i)
            additional_trees += sufficientarian_expected_tree_area[i, 0] - LGA[i, 43]
            sufficientarian_expected_tree_area[i, 0] = LGA[i, 43]


    sufficientarian_percentage = np.empty((sufficientarian_expected_tree_area.shape[0], 1), dtype=object)
    sufficientarian_percentage[:] = np.nan

    for i in range(sufficientarian_expected_tree_area.shape[0]):
        if i not in List_limited_veg_area:
            sufficientarian_percentage[i, 0] = sufficientarian_expected_tree_area[i, 0] / LGA[i, 3]
        else:
            sufficientarian_percentage[i, 0] = 1

    count = 0
    while count < LGA.shape[0]:
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
            allocation = (next_min_value - min_value) * LGA[min_indices[i], 3]
            if allocation > additional_trees:
                sufficientarian_percentage[min_indices[i], 0] = additional_trees / LGA[min_indices[i], 3] + min_value
                break
            additional_trees -= allocation
            sufficientarian_percentage[min_indices[i], 0] = next_min_value
        count += 1

    for i in range(sufficientarian_expected_tree_area.shape[0]):
        if i not in List_limited_veg_area:
            sufficientarian_expected_tree_area[i, 0] = LGA[i, 3] * sufficientarian_percentage[i, 0]



df_pred = pd.DataFrame(sufficientarian_expected_tree_area)
filepath_pred = 'LGA_Actual_MB_Sufficientarian_CS_Veg_(Sydney LGA).xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################

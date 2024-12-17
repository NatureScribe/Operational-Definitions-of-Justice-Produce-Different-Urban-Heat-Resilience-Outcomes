import numpy as np
import pandas as pd



############################ Calculate tree areas based on egalitarian theory of justice  ##############################

integrated_dataset = pd.read_excel("SA3_Integrated_Dataset_Filtered_Veg.xlsx")
integrated_dataset = np.asarray(integrated_dataset)

egalitarian_expected_tree_area = np.empty((integrated_dataset.shape[0], 1), dtype=object)
egalitarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(integrated_dataset[:, 2]) - sum(integrated_dataset[:, 3])
print(more_trees_sqm)

egal_ratio_tree = more_trees_sqm / sum(integrated_dataset[:, 1])
print(egal_ratio_tree)
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 3] + egal_ratio_tree * integrated_dataset[i, 1]

List_limited_veg_area = []
additional_trees = 1
total_available_area = sum(integrated_dataset[:, 1])

while additional_trees != 0:
    additional_trees = 0
    for i in range(egalitarian_expected_tree_area.shape[0]):
        if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 4]:
            List_limited_veg_area.append(i)
            additional_trees += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 4]
            total_available_area -= integrated_dataset[i, 1]
            egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 4]

    for i in range(egalitarian_expected_tree_area.shape[0]):
        if i not in List_limited_veg_area:
            egalitarian_expected_tree_area[i, 0] += additional_trees / total_available_area * integrated_dataset[i, 1]

df_pred = pd.DataFrame(egalitarian_expected_tree_area)
filepath_pred = 'Actual_SA3_Egalitarian_TreeArea_Veg.xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################

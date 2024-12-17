import numpy as np
import pandas as pd



############################ Calculate tree areas based on egalitarian theory of justice  ##############################

integrated_dataset = pd.read_excel("SA1_Integrated_Dataset_Filtered_Vul_Veg.xlsx")
integrated_dataset = np.asarray(integrated_dataset)

egalitarian_expected_tree_area = np.empty((integrated_dataset.shape[0], 1), dtype=object)
egalitarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(integrated_dataset[:, 2]) - sum(integrated_dataset[:, 3])
print(more_trees_sqm)

all_pop = sum(integrated_dataset[:, 7])
ratio_trees_persons = more_trees_sqm / all_pop

extra_trees = 0
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 3] + integrated_dataset[i, 7] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 4]:
        extra_trees += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 4]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 4]


for j in range(1000):
    ratio_trees_persons = extra_trees / all_pop
    extra_trees = 0
    for i in range(egalitarian_expected_tree_area.shape[0]):
        egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 7] * ratio_trees_persons
        if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 4]:
            extra_trees += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 4]
            egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 4]


df_pred = pd.DataFrame(egalitarian_expected_tree_area)
filepath_pred = 'Actual_SA1_Egalitarian_TreeArea_Vul_Veg.xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################

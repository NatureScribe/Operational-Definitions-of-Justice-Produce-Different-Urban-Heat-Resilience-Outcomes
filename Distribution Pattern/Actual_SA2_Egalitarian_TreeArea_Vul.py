import numpy as np
import pandas as pd



############################ Calculate tree areas based on egalitarian theory of justice  ##############################

integrated_dataset = pd.read_excel("SA2_Integrated_Dataset_Filtered_Vul.xlsx")
integrated_dataset = np.asarray(integrated_dataset)

egalitarian_expected_tree_area = np.empty((integrated_dataset.shape[0], 1), dtype=object)
egalitarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(integrated_dataset[:, 2]) - sum(integrated_dataset[:, 3])
print(more_trees_sqm)

all_pop = sum(integrated_dataset[:, 6])
ratio_trees_persons = more_trees_sqm / all_pop

extra_trees = 0
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 3] + integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees1 = 0
ratio_trees_persons = extra_trees / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees1 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees2 = 0
ratio_trees_persons = extra_trees1 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees2 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees3 = 0
ratio_trees_persons = extra_trees2 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees3 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees4 = 0
ratio_trees_persons = extra_trees3 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees4 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees5 = 0
ratio_trees_persons = extra_trees4 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees5 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees6 = 0
ratio_trees_persons = extra_trees5 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees6 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees7 = 0
ratio_trees_persons = extra_trees6 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees7 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees8 = 0
ratio_trees_persons = extra_trees7 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees8 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees9 = 0
ratio_trees_persons = extra_trees8 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees9 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]

extra_trees10 = 0
ratio_trees_persons = extra_trees9 / all_pop
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] += integrated_dataset[i, 6] * ratio_trees_persons
    if egalitarian_expected_tree_area[i, 0] > integrated_dataset[i, 1]:
        extra_trees10 += egalitarian_expected_tree_area[i, 0] - integrated_dataset[i, 1]
        egalitarian_expected_tree_area[i, 0] = integrated_dataset[i, 1]
        
        
df_pred = pd.DataFrame(egalitarian_expected_tree_area)
filepath_pred = 'Actual_SA2_Egalitarian_TreeArea_Vul.xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################

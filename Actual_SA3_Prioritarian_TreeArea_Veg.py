import numpy as np
import pandas as pd



############################ Calculate tree areas based on prioritarian theory of justice  ##############################

integrated_dataset = pd.read_excel("SA3_Integrated_Dataset_Filtered_Veg.xlsx")
integrated_dataset = np.asarray(integrated_dataset)

prioritarian_expected_tree_area = np.empty((integrated_dataset.shape[0], 1), dtype=object)
prioritarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(integrated_dataset[:, 2]) - sum(integrated_dataset[:, 3])
print(more_trees_sqm)

prio_weights = 0
for i in range(integrated_dataset.shape[0]):
    prio_weights += integrated_dataset[i, 1] - integrated_dataset[i, 3]
print(prio_weights)

for i in range(prioritarian_expected_tree_area.shape[0]):
    prioritarian_expected_tree_area[i, 0] = integrated_dataset[i, 3] + more_trees_sqm * (integrated_dataset[i, 1]-integrated_dataset[i, 3]) / prio_weights

List_limited_veg_area = []
additional_trees = 1
while additional_trees != 0:
    additional_trees = 0
    prio_weights = 0
    for i in range(prioritarian_expected_tree_area.shape[0]):
        if prioritarian_expected_tree_area[i, 0] > integrated_dataset[i, 4]:
            List_limited_veg_area.append(i)
            additional_trees += prioritarian_expected_tree_area[i, 0] - integrated_dataset[i, 4]
            prioritarian_expected_tree_area[i, 0] = integrated_dataset[i, 4]

    for i in range(integrated_dataset.shape[0]):
        if i not in List_limited_veg_area:
            prio_weights += integrated_dataset[i, 1] - prioritarian_expected_tree_area[i, 0]

    for i in range(prioritarian_expected_tree_area.shape[0]):
        if i not in List_limited_veg_area:
            prioritarian_expected_tree_area[i, 0] += additional_trees * (integrated_dataset[i, 1] - prioritarian_expected_tree_area[i, 0]) / prio_weights


df_pred = pd.DataFrame(prioritarian_expected_tree_area)
filepath_pred = 'Actual_SA3_Prioritarian_TreeArea_Veg.xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################

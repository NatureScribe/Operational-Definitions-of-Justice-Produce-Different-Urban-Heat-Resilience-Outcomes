import numpy as np
import pandas as pd



################ Calculate tree areas based on prioritarian theory of justice for LGAs independently  ###################
### First step ###
### Sample for Sydney LGA ###

# df = pd.read_excel('MB_Integrated_Dataset_Unfiltered.xlsx')
#
# sydney_rows = df[df['HEAT - LGA'] == 'Sydney']
# print(sydney_rows.shape)
# sydney_rows.to_excel('Sydney_LGA_MB_Integrated_Dataset_Unfiltered.xlsx', index=False)




########################################################################################################################
### Second step ###

LGA = pd.read_excel("Sydney_LGA_MB_Integrated_Dataset_Unfiltered.xlsx")
LGA = np.asarray(LGA)

prioritarian_expected_tree_area = np.empty((LGA.shape[0], 1), dtype=object)
prioritarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(LGA[:, 14]) - sum(LGA[:, 42])
print(more_trees_sqm)


prio_weights = 0
for i in range(LGA.shape[0]):
    prio_weights += LGA[i, 3] - LGA[i, 42]
print(prio_weights)

for i in range(prioritarian_expected_tree_area.shape[0]):
    prioritarian_expected_tree_area[i, 0] = LGA[i, 42] + more_trees_sqm * (LGA[i, 3]-LGA[i, 42]) / prio_weights

df_pred = pd.DataFrame(prioritarian_expected_tree_area)
filepath_pred = 'LGA_Actual_MB_Prioritarian_CP_(Sydney LGA).xlsx'
df_pred.to_excel(filepath_pred, index=False)



########################################################################################################################

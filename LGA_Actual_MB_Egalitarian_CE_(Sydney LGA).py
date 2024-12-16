import numpy as np
import pandas as pd



################ Calculate tree areas based on egalitarian theory of justice for LGAs independently  ###################
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

egalitarian_expected_tree_area = np.empty((LGA.shape[0], 1), dtype=object)
egalitarian_expected_tree_area[:] = np.nan

more_trees_sqm = sum(LGA[:, 14]) - sum(LGA[:, 42])
print(more_trees_sqm)

egal_ratio_tree = more_trees_sqm / sum(LGA[:, 3])
print(egal_ratio_tree)
for i in range(egalitarian_expected_tree_area.shape[0]):
    egalitarian_expected_tree_area[i, 0] = LGA[i, 42] + egal_ratio_tree * LGA[i, 3]
df_pred = pd.DataFrame(egalitarian_expected_tree_area)
filepath_pred = 'LGA_Actual_MB_Egalitarian_CE_(Sydney LGA).xlsx'
df_pred.to_excel(filepath_pred, index=False)


########################################################################################################################
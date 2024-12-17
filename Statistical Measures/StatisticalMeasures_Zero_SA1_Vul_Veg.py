import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error



########################## Calculate statistical measures for Zero distribution at SA1 level ############################

df = pd.read_excel('SA1_Integrated_Dataset_Filtered_Vul_Veg_Zero.xlsx')

def calculate_mad(dataset):
    mad = np.mean(np.abs(dataset))
    return mad

for column in ['Sufficientarian Difference', 'Egalitarian Difference', 'Prioritarian Difference']:
    df[column] = df[column] / 100
    dataset = df[column]
    mad = calculate_mad(dataset)
    print(f"Mean Absolute Deviation from {column}: {mad}")


columns_to_scale = [
    '2022 - Actual - more AREA_TREE/Hec',
    '2022 - Expected - Sufficientarian - more AREA_TREE/Hec',
    '2022 - Expected - Egalitarian - more AREA_TREE/Hec',
    '2022 - Expected - Prioritarian - more AREA_TREE/Hec'
]

# Scale down the specified columns by 100
for column in columns_to_scale:
    df[column] = df[column] / 100


mse_sufficientarian = mean_squared_error(df['2022 - Actual - more AREA_TREE/Hec'], df['2022 - Expected - Sufficientarian - more AREA_TREE/Hec'])
mse_egalitarian = mean_squared_error(df['2022 - Actual - more AREA_TREE/Hec'], df['2022 - Expected - Egalitarian - more AREA_TREE/Hec'])
mse_prioritarian = mean_squared_error(df['2022 - Actual - more AREA_TREE/Hec'], df['2022 - Expected - Prioritarian - more AREA_TREE/Hec'])

rmse_sufficientarian = np.sqrt(mse_sufficientarian)
rmse_egalitarian = np.sqrt(mse_egalitarian)
rmse_prioritarian = np.sqrt(mse_prioritarian)

print(f"RMSE - Sufficientarian: {rmse_sufficientarian}")
print(f"RMSE - Egalitarian: {rmse_egalitarian}")
print(f"RMSE - Prioritarian: {rmse_prioritarian}")


########################################################################################################################

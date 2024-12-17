# Operationalizing-Justice-in-Heat-Resilience-Building-Projects
This repository provides codes to compute statistical measures, distribution graphs, and deviations from justice (as detailed in the paper "Operationalizing Justice in Heat Resilience Building Projects"). Deviations are processed in Excel to calculate percentage differences and then input into ArcGIS for visualization.

# Dataset instructions
The datasets in this repository are provided in two formats:

1. **Directly downloadable files**:  
   - Some datasets are uploaded as `.xlsx` files and are ready to be used directly as input into the Python scripts.

2. **Split archives**:  
   - Larger datasets are divided into multiple parts due to GitHub’s file size limitations. These files are provided in `.Z01`, `.Z02`, and `.zip` formats.

## Steps for extracting split archives
1. Download all parts (e.g., `.Z01`, `.Z02`, `.zip`) for the required dataset from the repository.
2. Ensure all parts of the dataset are stored in the same folder.
3. Use **WinRAR** or **7-Zip** to extract the archive:
   - Right-click on the `.zip` file (e.g., `DatasetName.zip`) and select **Extract Here** or **Extract to [folder name]**.
   - The tool will automatically combine the split parts and extract the complete dataset.
4. Once extracted, ensure the dataset is in `.xlsx` format to make it ready for use as input into the Python scripts.

### Notes:
- All parts (e.g., `.Z01`, `.Z02`, etc.) are required for successful extraction.
- If extraction fails, ensure that all parts have been downloaded and placed in the same folder.

# File naming convention
## In Python files (`.py`):
The repository uses systematic file naming conventions to indicate the **scenario**, **justice theory**, **granularity level**, **spatial scale**, **task**, and additional **attributes** processed in each file.

- **Scenario**:
  - `Zero`: Represents a baseline or reference scenario (zero distribution).
  - `Actual`: Represents the actual distribution of tree canopies between 2016 and 2022 (actual distribution).

...

# In Excel files (`.xlsx`):
The naming convention for Excel files follows that of Python files, with additional features to indicate **integration status** and **data refinement status**.

- **Integration status**:
  - `Integrated`: Indicates that all data is combined into a single file, and the Python script's output is included in the last columns without interfering with input columns.

- **Data refinement status**:
  - `Filtered`: Contains only columns that are directly useful for analysis or future studies.
  - `Unfiltered`: Includes all information, including data preprocessing steps and columns that might not be necessary for immediate analysis.

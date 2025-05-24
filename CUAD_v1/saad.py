import pandas as pd
import os

# 1. Set your folder path
folder_path = 'label_group_xlsx'

# 2. Get all Excel files from the folder
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 2. Read each file and store DataFrames
dfs = []
for file in all_files:
    df = pd.read_excel(file)
    if 'Filename' in df.columns:
        dfs.append(df)

if dfs:
    # 3. Merge vertically on Filename
    merged = pd.concat(dfs).reset_index(drop=True)
    
    # 4. Group by Filename and aggregate other columns
    # This will combine values while removing duplicates
    def combine_unique(x):
        if pd.api.types.is_numeric_dtype(x):
            return x.drop_duplicates().max()  # For numeric columns, take max
        else:
            # For text columns, combine unique values with comma separator
            unique_values = x.dropna().unique()
            return ', '.join(str(val) for val in unique_values) if len(unique_values) > 0 else pd.NA

    final_merged = merged.groupby('Filename').agg(combine_unique).reset_index()
    
    final_merged['Filename'] = final_merged['Filename'].str.replace(r'\.pdf$', '', case=False, regex=True)
    # 5. Save the result
    final_merged.to_excel('merged_files.xlsx', index=False)
    print(f"Merged {len(dfs)} files. Total rows after merging: {len(final_merged)}")
    print(f"Original rows before merging: {len(merged)}")
else:
    print("No files with 'Filename' column found")

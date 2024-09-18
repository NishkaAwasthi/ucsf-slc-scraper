import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('formatted_output.csv')
df2 = pd.read_csv('raw_output_web_scraping.csv')

# Rename columns for merging
df1.rename(columns={df1.columns[0]: 'merge_key'}, inplace=True)
df2.rename(columns={df2.columns[1]: 'merge_key'}, inplace=True)

# Merge the DataFrames on the renamed 'merge_key' column
merged_df = pd.merge(df1, df2, on='merge_key')

# Optionally, save the merged DataFrame to a new CSV file
merged_df.to_csv('FINAL_FILE.csv', index=False)
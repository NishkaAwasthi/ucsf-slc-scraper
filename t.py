import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('FINAL_FILE.csv')

# Print all headers of the new merged DataFrame
print("Headers of the merged DataFrame:")
print(df1.columns.tolist())

columns_to_remove = ['XRAY/EM']  # replace with actual column names

# Drop the columns from the merged DataFrame
filtered_df = df1.drop(columns=columns_to_remove)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('FINAL_FILE_filtered.csv', index=False)
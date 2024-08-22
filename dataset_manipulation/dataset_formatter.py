import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('cleaned_output.csv')

# Fill missing Entry ID values with the value from the row above
df['Entry ID'] = df['Entry ID'].ffill()

# Group by 'Entry ID' and forward-fill missing values within each group
df = df.groupby('Entry ID', group_keys=False).apply(lambda group: group.ffill())

# Remove duplicate rows
df = df.drop_duplicates()

# Reset index to remove any multi-index
df = df.reset_index(drop=True)

# Explicitly infer objects to avoid dtype warnings
df = df.infer_objects()

# Save the updated DataFrame to a new CSV file
df.to_csv('formatted_output.csv', index=False)

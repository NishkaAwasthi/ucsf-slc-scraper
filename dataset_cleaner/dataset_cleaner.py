import pandas as pd

def filter_csv(input_file_path: str, output_file_path: str):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file_path)
    
    # Identify the last column name
    last_column = df.columns[-1]
    
    # Filter out rows where only the last column has non-NaN values
    df_filtered = df[~df[df.columns[:-1]].isna().all(axis=1)]
    
    # Write the filtered DataFrame to a new CSV file
    df_filtered.to_csv(output_file_path, index=False)

# Example usage
input_csv = 'raw_output.csv'
output_csv = 'cleaned_output.csv'
filter_csv(input_csv, output_csv)
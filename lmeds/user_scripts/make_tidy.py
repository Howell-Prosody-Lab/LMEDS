"""
Created May 25 2026
@author: slittle95
"""

from tkinter import filedialog
import pandas as pd


keepAsking = True
file_list = []
while keepAsking:
    f = filedialog.askopenfile(title="Choose file")
    file_list.append(f)
    print (str(f))
    q = input("Add another? y/n")
    if q.lower() != 'y':
        keepAsking = False

number_of_files = len(file_list)
print(number_of_files)
df_list = []
for f in file_list:
    df = pd.read_csv(f)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Remove the row at index 0 (secondary header)
    df = df.drop(index=0).reset_index(drop=True)
    # Define id_vars and value_vars for pivoting
    id_vars = df.columns[:4].tolist()
    value_vars = df.columns[4:].tolist()
    # Pivot
    df_melted = df.melt(id_vars=id_vars, value_vars=value_vars, var_name='Metric_and_ID', value_name='Value')
    print(df.head())
    df_list.append(df_melted)

combined_df = pd.concat(df_list, ignore_index=True)
combined_df[['ID', 'Metric_Type']] = combined_df['Metric_and_ID'].str.split('.', expand=True)
combined_df = combined_df.drop(columns=['Metric_and_ID'])
combined_df['Variety'] = combined_df['ID'].str[0].fillna('')
combined_df['Gender'] = combined_df['ID'].str[1].fillna('')
# Reorder columns to move 'Value' to the end
# Get all columns except 'Value'
other_cols = [col for col in combined_df.columns if col != 'Value']
# Append 'Value' at the end
combined_df = combined_df[other_cols + ['Value']]
combined_df.to_csv('all_boundary_and_prominence.csv')





import os
import pandas as pd

# Directory containing the labeled data
data_directory = './'

# # List of dataset files
# dataset_files = [
#     'benign_update_benign.csv',
#     'bruteforce_update_bruteforce.csv',
#     'ddos_update_ddos.csv',
#     'probe_update_nmap.csv',
#     'sqlattack_update_sqlattack.csv'
# ]
dataset_files = [
    'bruteforce_cleaned_bruteforce.csv',
    'ipdos_cleaned_ipdos.csv'
]

# Create an empty DataFrame to store the aggregated data
master_dataset = pd.DataFrame()

# Iterate through the dataset files and concatenate them
for file in dataset_files:
    file_path = os.path.join(data_directory, file)
    df = pd.read_csv(file_path)
    master_dataset = pd.concat([master_dataset, df], ignore_index=True)

# Save the aggregated dataset to a new CSV file
master_dataset.to_csv('master_dataset.csv', index=False)

print("Master dataset has been created: master_dataset.csv")

import pandas as pd


filename = "ipdos.csv"
file1 = pd.read_csv(filename)
file1.head(10)
file1.isnull().sum

# step-1 to replace all null
update_file = file1.fillna(" ")
update_file.isnull().sum()

# step-2 to remove all rows with null value
update_file = file1.fillna(0)


df = pd.read_csv('ipdos_cleaned_ipdos.csv')
data_type = df.iloc[206, 7].dtype
print("RESULT:", data_type)




# update_file.to_csv('test_'+filename, index = False)
import os
import pandas as pd

os.chdir("/data/project/ubrite/drg-depot/data_folder") # cd in linux

os.listdir() # ls in linux

data = pd.read_csv("data_file.csv")

# PRE-CLEANING EXPLORATORY DATA ANALYSIS

# display the first few rows of the DataFrame
print("First few rows:")
print(data.head())

# check the dimensions of the DataFrame
print("Data shape:")
print(data.shape)

# check the column names
print("Column names:")
print(data.columns)

# check the data types of each column
print("Data types:")
print(data.dtypes)

# check for missing values
print("Missing values:")
print(data.isnull().sum())

# perform summary statistics
print("Summary statistics:")
print(data.describe())

# perform correlation analysis
print("Correlation analysis:")
print(data.corr())

# OUTLIER REMOVAL

# Define the column(s) to remove outliers from
column_to_check = 'column_name'

# Calculate the IQR boundaries
Q1 = data[column_to_check].quantile(0.25)
Q3 = data[column_to_check].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
filtered_data = data[(data[column_to_check] >= lower_bound) & (data[column_to_check] <= upper_bound)]

# DATA CLEANING

# reengineer string columns (look on ChatGPT)

# convert columns with mixed data types to appropriate types
# data['column1'] = pd.to_numeric(data['column1'], errors='coerce')
# data['column2'] = pd.to_datetime(data['column2'], errors='coerce')

# remove a prefix from a string column
# num_chars = 10
# data["column1"] = data['column1'].astype(str).str[num_chars:]

# drop duplicates
data.drop_duplicates(inplace=True)

# drop rows with null values (be careful of data loss)
# data.dropna(inplace=True)

# rename a pandas column
data.rename(columns={'old_column_name':'new_column_name'}, inplace=True)

# NORMALIZATION

# Define the columns to normalize
columns_to_normalize = ['column1', 'column2', 'column3']

# Apply min-max normalization
data[columns_to_normalize] = (data[columns_to_normalize] - data[columns_to_normalize].min()) / (data[columns_to_normalize].max() - data[columns_to_normalize].min())

# POST-CLEANING EXPLORATORY DATA ANALYSIS

# display the first few rows of the DataFrame
print("First few rows:")
print(data.head())

# check the dimensions of the DataFrame
print("Data shape:")
print(data.shape)

# check the column names
print("Column names:")
print(data.columns)

# check the data types of each column
print("Data types:")
print(data.dtypes)

# check for missing values
print("Missing values:")
print(data.isnull().sum())

# perform summary statistics
print("Summary statistics:")
print(data.describe())

# perform correlation analysis
print("Correlation analysis:")
print(data.corr())

# save the cleaned data to a new CSV file
data.to_csv('cleaned_file.csv', index=False)
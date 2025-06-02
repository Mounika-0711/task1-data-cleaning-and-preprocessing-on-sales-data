
# Task 1: Data Cleaning and Preprocessing – Sales Data using Python (Pandas)

import pandas as pd

# Step 1: Load Dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Step 2: Check for Missing Values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Step 3: Remove Missing and Duplicate Rows
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Step 4: Standardize Text Values
df['country'] = df['country'].str.strip().str.upper()
df['status'] = df['status'].str.strip().str.title()

# Step 5: Convert Date Format
df['orderdate'] = pd.to_datetime(df['orderdate'])
df['orderdate'] = df['orderdate'].dt.strftime('%d-%m-%Y')

# Step 6: Rename Column Headers
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 7: Check and Fix Data Types
print("Data types after cleaning:")
print(df.dtypes)

# Step 8: Final Dataset Information
print("Cleaned dataset info:")
print(df.info())

# Step 9: Save Cleaned Data
df.to_csv("cleaned_sales_data1.csv", index=False)

# Step 10: Download the Cleaned File (for Google Colab users)
from google.colab import files
files.download("cleaned_sales_data1.csv")

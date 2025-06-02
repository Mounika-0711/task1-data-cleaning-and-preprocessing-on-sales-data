# Task 1: Data Cleaning and Preprocessing – Sales Data

# Objective:

Clean and prepare a raw sales dataset using Python (Pandas) in Google Colab. This includes handling null values, removing duplicates, standardizing formats, and exporting the cleaned dataset.


# Dataset Used:

File: sales_data_sample (1).csv

Source: https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

Encoding: latin1

Dataset downloaded from Kaggle and uploaded to Google Colab manually

---

# Steps Performed:

1. Load Dataset

import pandas as pd
df = pd.read_csv("sales_data_sample (1).csv", encoding='latin1')

2. Missing Value Check

df.isnull().sum()

3. Remove Duplicates

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

4. Standardize Text Columns

df['country'] = df['country'].str.strip().str.upper()
df['status'] = df['status'].str.strip().str.title()

5. Convert Dates

df['orderdate'] = pd.to_datetime(df['orderdate'])
df['orderdate'] = df['orderdate'].dt.strftime('%d-%m-%Y')

6. Rename Columns

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

7. Data Type Check

df.dtypes

# Final Output:

Cleaned dataset saved as: cleaned_sales_data1.csv

Downloaded from Google Colab:
from google.colab import files  
files.download("cleaned_sales_data1.csv")

# Summary of Changes:

* Missing Values checked and dropped rows with nulls
* Duplicate Rows removed duplicates
* Text Standardization cleaned & formatted text (country, status)
* Date Format	Converted to dd-mm-yyyy
* Column Names renamed to lowercase_with_underscores
* Data Types verified and adjusted where needed


# Tools Used:

Python

Pandas

Google Colab


# Author:

SHENAGARAPU MOUNIKA

GitHub: http://github.com/Mounika-0711

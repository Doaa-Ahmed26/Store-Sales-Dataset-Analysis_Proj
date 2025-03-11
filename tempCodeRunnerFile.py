import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'G:\do\Learn\رواد\Lectures\First Version\Superstore Sales Dataset.csv'
data = pd.read_csv(file_path)


# Convert date columns to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")

# Handle missing Postal Code values (fill with 'Unknown')
df["Postal Code"] = df["Postal Code"].fillna("Unknown")

# Drop the unnecessary 'Row ID' column
df = df.drop(columns=["Row ID"])

# Remove rows with missing values
df_cleaned = df.dropna()

# Detect and remove outliers using IQR
Q1 = df_cleaned.quantile(0.25, numeric_only=True)
Q3 = df_cleaned.quantile(0.75, numeric_only=True)
IQR = Q3 - Q1
df_no_outliers = df_cleaned[~((df_cleaned < (Q1 - 1.5 * IQR)) | (df_cleaned > (Q3 + 1.5 * IQR))).any(axis=1)]

# Save cleaned dataset
df_no_outliers.to_csv("G:\do\Learn\رواد\Lectures\Project\Cleaned_Superstore_Sales.csv", index=False)

# Display basic info
df_no_outliers.info()
print(df_no_outliers.head())

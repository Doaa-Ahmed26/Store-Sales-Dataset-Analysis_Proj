import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'G:\do\Learn\رواد\Lectures\Project\Superstore Sales Dataset.csv'
data = pd.read_csv(file_path)

# Convert date columns to datetime format
data["Order Date"] = pd.to_datetime(data["Order Date"], format="%d/%m/%Y")
data["Ship Date"] = pd.to_datetime(data["Ship Date"], format="%d/%m/%Y")

data = data.drop(columns=["Row ID"])

data_cleaned = data.dropna()

# Detect and remove outliers using IQR
numeric_columns = data_cleaned.select_dtypes(include=[np.number]).columns
Q1 = data_cleaned[numeric_columns].quantile(0.25)
Q3 = data_cleaned[numeric_columns].quantile(0.75)
IQR = Q3 - Q1

Clean_data = data_cleaned[~((data_cleaned[numeric_columns] < (Q1 - 1.5 * IQR)) | (data_cleaned[numeric_columns] > (Q3 + 1.5 * IQR))).any(axis=1)]

Clean_data.to_csv("G:\do\Learn\رواد\Lectures\Project\Cleaned_Superstore_Sales.csv", index=False)

Clean_data.info()
print(Clean_data.head())

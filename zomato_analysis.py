import pandas as pd

# Load Zomato data
zomato_data_path = f"C:\Users\erani\Desktop\Zomato Data Analysis\Zamoto raw data\zomato.csv"
zomato_df = pd.read_csv(zomato_data_path, encoding='unicode_escape')

# Load Country Code data
country_code_path = f"C:\Users\erani\Desktop\Zomato Data Analysis\Zamoto raw data\Country-Code.xlsx"
country_df = pd.read_excel(country_code_path)

# Data Cleaning for Zomato Data
print("Zomato Data Info:")
print(zomato_df.info())

print("Null Values in Zomato Data:")
print(zomato_df.isnull().sum())

print("Top 10 rows of Zomato Data:")
print(zomato_df.head(10))

print("Description of Zomato Data:")
print(zomato_df.describe())

print("Duplicates in Zomato Data:")
print(zomato_df.duplicated().sum())

print("Columns Names in Zomato Data:")
print(zomato_df.columns)

print("Data Types in Zomato Data:")
print(zomato_df.dtypes)

print("Shape of Zomato Data:")
print(zomato_df.shape)

# Data Cleaning for Country Code Data
print("Country Code Data Info:")
print(country_df.head())

print("Info of Country Code Data:")
print(country_df.info())

print("Shape of Country Code Data:")
print(country_df.shape)

print("Null Values in Country Code Data:")
print(country_df.isnull().sum())

print("Duplicates in Country Code Data:")
print(country_df.duplicated().sum())

# Merging Zomato data with Country Code data
merged_df = pd.merge(zomato_df, country_df, on='Country Code', how='left')
print("Merged Data:")
print(merged_df.head())

# Dropping unwanted columns
merged_df.drop(['Restaurant ID', 'Locality Verbose', 'Country Code', 'Longitude', 'Latitude'], axis=1, inplace=True)
print("Columns after dropping:")
print(merged_df.columns)

# Checking null values after merging
print("Null Values after merging:")
print(merged_df.isnull().sum())

# Removing null values
cleaned_df = merged_df.dropna()
print("Null Values after removal:")
print(cleaned_df.isnull().sum())

# Counting total transactions in all countries
print("Total transactions in each country:")
print(cleaned_df['Country'].value_counts())

# Save cleaned data
cleaned_df.to_csv("cleaned zomato data.csv", index=False)

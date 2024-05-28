import pandas as pd

googlePlay_df=pd.read_csv('googleplaystore.csv')

print(googlePlay_df.columns)

missing_values = googlePlay_df.isnull().sum()


## Now we will drop the missing value
## here inplace is use to make it permanent
googlePlay_df.dropna(inplace=True)

# 2. Removing Duplicates
# Check for and remove duplicate rows
duplicate_rows = googlePlay_df.duplicated().sum()


# Remove duplicate rows
googlePlay_df.drop_duplicates(inplace=True)

# 3. Standardizing Formats (if necessary)
# No specific standardization required in this case

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(googlePlay_df.head())
print("Summary about the Data: ")
print(googlePlay_df.describe())


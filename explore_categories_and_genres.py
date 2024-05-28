import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
googlePlay_df = pd.read_csv('googleplaystore.csv')

# Remove duplicate rows
googlePlay_df.drop_duplicates(inplace=True)

# Drop rows with missing values
googlePlay_df.dropna(inplace=True)

# Explore the distribution of apps across different categories
category_counts = googlePlay_df['Category'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette="viridis")
plt.title('Distribution of Apps Across Categories')
plt.xlabel('Category')
plt.ylabel('Number of Apps')
plt.xticks(rotation=90)
plt.show()

# Explore the distribution of apps across different genres
# Split the genres and count the occurrences of each genre
genres_counts = googlePlay_df['Genres'].str.split(';', expand=True).stack().value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=genres_counts.values, y=genres_counts.index, palette="viridis")
plt.title('Distribution of Apps Across Genres')
plt.xlabel('Number of Apps')
plt.ylabel('Genre')

plt.show()

# Analyze the popularity of categories based on the number of user installs
# Convert installs to numeric by removing '+' and ',' and converting to integer
googlePlay_df['Installs'] = googlePlay_df['Installs'].str.replace('+', '').str.replace(',', '').astype(int)

category_installs = googlePlay_df.groupby('Category')['Installs'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=category_installs.values, y=category_installs.index, palette="viridis")
plt.title('Popularity of Categories Based on User Installs')
plt.xlabel('Number of Installs')
plt.ylabel('Category')
plt.show()

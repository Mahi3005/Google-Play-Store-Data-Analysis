import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
googlePlay_df = pd.read_csv('googleplaystore.csv')

# Remove duplicate rows
googlePlay_df.drop_duplicates(inplace=True)

# Drop rows with missing values
googlePlay_df.dropna(inplace=True)

# Convert installs to numeric by removing '+' and ',' and converting to integer
googlePlay_df['Installs'] = googlePlay_df['Installs'].str.replace('+', '').str.replace(',', '').astype(int)

# Calculate summary statistics
free_apps_installs = googlePlay_df[googlePlay_df['Type'] == 'Free']['Installs']
paid_apps_installs = googlePlay_df[googlePlay_df['Type'] == 'Paid']['Installs']

mean_free_installs = free_apps_installs.mean()
median_free_installs = free_apps_installs.median()
mean_paid_installs = paid_apps_installs.mean()
median_paid_installs = paid_apps_installs.median()

print(f"Free Apps - Mean Installs: {mean_free_installs}, Median Installs: {median_free_installs}")
print(f"Paid Apps - Mean Installs: {mean_paid_installs}, Median Installs: {median_paid_installs}")

# Box plot to compare the distribution of installs for free and paid apps
plt.figure(figsize=(12, 8))
sns.boxplot(x='Type', y='Installs', data=googlePlay_df, palette="viridis")
plt.title('Distribution of Installs for Free and Paid Apps')
plt.xlabel('App Type')
plt.ylabel('Number of Installs')
plt.yscale('log')  # Using log scale for better visualization
plt.show()

# Bar plot to compare the average installs for free and paid apps
avg_installs = googlePlay_df.groupby('Type')['Installs'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='Type', y='Installs', data=avg_installs, palette="viridis")
plt.title('Average Number of Installs for Free and Paid Apps')
plt.xlabel('App Type')
plt.ylabel('Average Number of Installs')
plt.yscale('log')  # Using log scale for better visualization
plt.show()

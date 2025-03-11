import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_youtube_data.csv')
df = df.sort_values(by='publish_date')

# Convert dates to datetime format
df['publish_date'] = pd.to_datetime(df['publish_date'])

# Plot views over time
daily_views = df.groupby('publish_date')['views'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(daily_views['publish_date'], daily_views['views'], 'o-', label="Average Views")
plt.xlabel('Publish Date')
plt.ylabel('Average Views')
plt.title('Average Views Over Time')
plt.legend()

# Save the plot as an image before displaying it
plt.savefig('time_series_plot.png')
plt.close()  # Close the plot to avoid reusing the same figure context

# Plot distribution of views
plt.figure(figsize=(10, 6))
sns.histplot(df['views'], bins=20, kde=True)
plt.title('Distribution of Views')
plt.xlabel('Views')
plt.ylabel('Frequency')

# Save the plot as an image before displaying it
plt.savefig('distribution_plot.png')
plt.close()

# Correlation matrix
corr_matrix = df[['views', 'likes', 'comments']].corr()

# Heatmap of correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')

# Save the heatmap as an image before displaying it
plt.savefig('correlation_matrix.png')
plt.close()

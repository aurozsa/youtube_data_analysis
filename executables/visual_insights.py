import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the cleaned dataset
df = pd.read_csv('cleaned_youtube_data.csv')

# Convert dates to datetime format
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')
df = df.sort_values(by='publish_date')

# Directory to save plots
output_dir = '../assets/img/'  # Path to save plots
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Plot: Average Views Over Time
plt.figure(figsize=(10, 6))
daily_views = df.groupby('publish_date')['views'].mean().reset_index()
plt.plot(daily_views['publish_date'], daily_views['views'], 'o-', label="Average Views")
plt.xlabel('Publish Date')
plt.ylabel('Average Views')
plt.title('Average Views Over Time')
plt.legend()
plt.savefig(f"{output_dir}average_views_over_time.png")
plt.close()

# Plot: Distribution of Views
plt.figure(figsize=(10, 6))
sns.histplot(df['views'], bins=20, kde=True)
plt.title('Distribution of Views')
plt.xlabel('Views')
plt.ylabel('Frequency')
plt.savefig(f"{output_dir}distribution_of_views.png")
plt.close()

# Correlation Matrix
corr_matrix = df[['views', 'likes', 'comments']].corr()

# Heatmap of Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig(f"{output_dir}correlation_matrix.png")
plt.close()

# Additional Plot: Views by Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='category_name', y='views', data=df)
plt.title('Views by Category Name')
plt.xticks(rotation=45)
plt.savefig(f"{output_dir}views_by_category_boxplot.png")
plt.close()

# Additional Plot: Engagement Metrics (Likes per View Distribution)
df['likes_per_view'] = df['likes'] / df['views']
plt.figure(figsize=(10, 6))
sns.histplot(df['likes_per_view'], bins=30, kde=True)
plt.title('Distribution of Likes Per View')
plt.xlabel('Likes per View')
plt.ylabel('Frequency')
plt.savefig(f"{output_dir}likes_per_view_distribution.png")
plt.close()

print(f"Plots have been saved to {output_dir}")

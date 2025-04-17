import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv('cleaned_youtube_data.csv')

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Directory to save plots
output_dir = '../assets/img/'  # Relative path to 'assets/img' folder

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Distribution of Numeric Features
plt.figure()
df['views'].hist(bins=30)
plt.title('Distribution of Views')
plt.xlabel('Views')
plt.ylabel('Frequency')
plt.savefig(f"{output_dir}distribution_of_views.png")
plt.close()

# Correlation Matrix
plt.figure()
corr_matrix = df[['views', 'likes', 'comments']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig(f"{output_dir}correlation_matrix.png")
plt.close()

# Scatter Plot: Views vs. Likes
plt.figure()
plt.scatter(df['views'], df['likes'], alpha=0.5)
plt.title('Views vs. Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.savefig(f"{output_dir}views_vs_likes_scatterplot.png")
plt.close()

# Boxplot: Views by Category
plt.figure()
sns.boxplot(x='category_name', y='views', data=df)
plt.title('Views by Category Name')
plt.xticks(rotation=45)
plt.savefig(f"{output_dir}views_by_category_boxplot.png")
plt.close()

# Time-Based Analysis
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')

plt.figure()
daily_views = df.groupby(df['publish_date'].dt.date)['views'].sum()
daily_views.plot()
plt.title('Total Views Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Total Views')
plt.savefig(f"{output_dir}total_views_over_time.png")
plt.close()

# Engagement Metrics
plt.figure()
df['likes_per_view'] = df['likes'] / df['views']
df['comments_per_view'] = df['comments'] / df['views']
sns.histplot(df['likes_per_view'], kde=True)
plt.title('Distribution of Likes per View')
plt.savefig(f"{output_dir}likes_per_view_distribution.png")
plt.close()

# Save the enhanced dataset to CSV
df.to_csv('cleaned_youtube_data_with_eda.csv', index=False)
print(f"Plots saved to '{output_dir}' and data saved to 'cleaned_youtube_data_with_eda.csv'.")

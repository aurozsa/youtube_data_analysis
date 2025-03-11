import pandas as pd

# Load dataset
df = pd.read_csv('youtube_trending_videos.csv')

# Handle missing values by directly reassigning the modified columns
df['likes'] = df['likes'].fillna(0)
df['comments'] = df['comments'].fillna(0)

# Format dates
df['publish_date'] = pd.to_datetime(df['publish_date'])
df['trending_date'] = pd.to_datetime(df['trending_date'])

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv('cleaned_youtube_data.csv', index=False)
print("Cleaned data saved to cleaned_youtube_data.csv")

import pandas as pd

# Load cleaned data
df = pd.read_csv('cleaned_youtube_data.csv')

# Summary statistics
print("Summary Statistics:")
print(df.describe())

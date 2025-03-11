import requests
import pandas as pd
import json

# Load API key from api_key.txt
try:
    with open('api_key.txt', 'r') as file:
        api_key = file.read().strip()
except FileNotFoundError:
    raise FileNotFoundError("api_key.txt file not found. Please ensure it exists in the project folder.")

# Base URL for YouTube Data API
base_url = 'https://www.googleapis.com/youtube/v3/videos'

# Parameters for the API request
params = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'regionCode': 'US',
    'videoCategoryId': '10',  # Music category
    'maxResults': 50,
    'key': api_key
}

# Make the API request
response = requests.get(base_url, params=params)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant information and store it in a DataFrame
    video_data = []
    for video in data['items']:
        video_info = {
            'title': video['snippet']['title'],
            'channel': video['snippet']['channelTitle'],
            'views': int(video['statistics']['viewCount']),
            'likes': int(video['statistics'].get('likeCount', 0)),
            'comments': int(video['statistics'].get('commentCount', 0)),
            'publish_date': video['snippet']['publishedAt'],
            'trending_date': pd.Timestamp.now()
        }
        video_data.append(video_info)

    # Save the data to a CSV file
    df = pd.DataFrame(video_data)
    df.to_csv('youtube_trending_videos.csv', index=False)
    print("Data successfully saved to youtube_trending_videos.csv")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

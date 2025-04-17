import requests
import pandas as pd
import time  # To add delays if needed

# Relative path to api_key.txt
with open('../api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Base URL and parameters
base_url = 'https://www.googleapis.com/youtube/v3/videos'
params = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'maxResults': 50,
    'key': api_key
}

# Function to fetch category details
def fetch_categories(api_key, region_code='US'):
    url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={region_code}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        categories = {item['id']: item['snippet']['title'] for item in data['items']}
        return categories
    else:
        print(f"Error: Unable to fetch categories. Status code: {response.status_code}")
        return None

# Fetch categories (once, at the beginning)
region_code = 'US'
categories = fetch_categories(api_key, region_code)

# Initialize variables
video_data = []
next_page_token = None

# Loop to fetch multiple pages of results
while len(video_data) < 500:
    if next_page_token:
        params['pageToken'] = next_page_token

    response = requests.get(base_url, params=params)

    # Check for errors
    if response.status_code != 200:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        print(response.json())  # Print error details
        break

    # Parse the JSON response
    data = response.json()

    # Debug: Print the number of items fetched in this batch
    print(f"Fetched {len(data.get('items', []))} videos")

    # Extract video information
    for video in data.get('items', []):
        category_id = video['snippet'].get('categoryId', None)
        category_name = categories.get(category_id, 'Unknown') if categories else 'Unknown'

        video_info = {
            'title': video['snippet']['title'],
            'channel': video['snippet']['channelTitle'],
            'views': int(video['statistics'].get('viewCount', 0)),
            'likes': int(video['statistics'].get('likeCount', 0)),
            'comments': int(video['statistics'].get('commentCount', 0)),
            'publish_date': video['snippet']['publishedAt'],
            'trending_date': pd.Timestamp.now(),
            'category_id': category_id,
            'category_name': category_name
        }
        video_data.append(video_info)

        # Stop if we've reached 500 videos
        if len(video_data) >= 500:
            print("Reached the limit of 500 videos. Stopping data collection.")
            break  # Break out of the inner loop

    # Get the next page token
    next_page_token = data.get('nextPageToken')

    # Debug: Print the nextPageToken
    print(f"Next Page Token: {next_page_token}")

    # Stop fetching if no more pages
    if not next_page_token:
        print("No more pages available")
        break

    # Optional: Add a delay to avoid hitting API limits
    time.sleep(1)

# Save the data to a CSV file
df = pd.DataFrame(video_data[:500])  # Limit to 500 rows
df.to_csv('youtube_trending_videos.csv', index=False)
print("Data successfully saved to youtube_trending_videos.csv")

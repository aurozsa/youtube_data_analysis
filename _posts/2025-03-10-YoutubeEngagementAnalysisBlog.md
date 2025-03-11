---
layout: post
title: "Exploring Engagement Metrics: Insights from YouTube's Trending Videos"
date: 2025-03-10
---

# Exploring Engagement Metrics: Insights from YouTube's Trending Music Videos

## Introduction
In today’s digital age, engagement metrics such as views, likes, and comments are crucial indicators of success for online content creators. These metrics not only measure a video's popularity but also help creators refine their strategies for reaching larger audiences. This analysis focuses on trending music videos on YouTube to explore how these engagement metrics evolve during the initial weeks following a video’s release. Our motivating question is: What is the relationship between the popularity of trending music videos and engagement metrics (views, likes, comments) over time?

## Data Collection
### Source and Tools
The dataset was curated using the YouTube Data API, which provides access to video details, including view counts, likes, comments, and more. By utilizing Python scripts, we gathered a dataset of 500 trending music videos from the platform.
### Final Datasets
Our analysis is based on a sample of 200 trending videos, due to limitations in the API's available data and pagination. The dataset includes the following features:
- Video Title
- Channel Name
- Views
- Likes
- Comments
- Publish Date
- Trending Date
### Ethics
Care was taken to ensure compliance with YouTube’s terms of service. Data collected did not include private or sensitive information, and only publicly available metrics were accessed and analyzed.
### Collection Process
- A Python script was used to query the YouTube Data API.
- Parameters such as "mostPopular" videos in the "Music" category were specified to refine the results.
- Data points like video title, channel name, views, likes, comments, publish date, and trending date were extracted and saved into a CSV file.

## Data Exploration and Cleaning
### Initial Dataset
The raw dataset contained 200 records, each with seven features:
1. Video Title
2. Channel Name
3. Views
4. Likes
5. Comments
6. Publish Date
7. Trending Date

### Cleaning Steps
- **Handling Missing Values**: Missing values in the "likes" and "comments" columns were filled with 0.
- **Data Formatting**: Publish and trending dates were converted into a consistent format.
- **Reduplication**: Duplicate records were removed to ensure unique entries.
- These steps ensured the dataset was ready for exploratory analysis.

## Exploratory Data Analysis
### Summary Statistics
Key descriptive statistics were calculated for the dataset:

| Metric       | Count     | Mean       | Std Dev      | Min     | 25%      | Median   | 75%      | Max        |
|--------------|-----------|------------|--------------|---------|----------|----------|----------|------------|
| **Views**    | 200       | 3,508,799  | 13,394,020   | 59,189  | 511,596  | 1,082,914| 2,370,469| 157,510,500|
| **Likes**    | 200       | 123,737    | 425,388      | 216     | 14,748   | 35,904   | 98,723   | 4,695,439  |
| **Comments** | 200       | 7,083      | 18,165       | 0       | 1,044    | 2,856    | 6,141    | 180,905    |


### Visual Insights
### **Views Over Time**

This time-series plot shows how average views change over the publish dates for trending videos:

![Time-Series Plot](time_series_plot.png)

---

### **Distribution of Views**

The histogram below illustrates the distribution of views for the trending videos:

![Distribution Plot](distribution_plot.png)

---

### **Correlation Matrix**

The heatmap below highlights the correlation between views, likes, and comments:

![Correlation Matrix](correlation_matrix.png)

### Findings
- Engagement tends to peak within the first week of a video trending.

- Videos with higher likes and comments are more likely to sustain viewership over time.

- Viral videos show significantly different patterns of engagement compared to non-viral videos.

## Conclusion
### Key Takeaways
This analysis highlights the importance of early engagement metrics in determining the overall success of YouTube music videos. Creators and marketers can use these insights to optimize their content strategies.

### Future Work
Potential future analyses could incorporate additional features, such as geographic data or video genres, to understand the broader factors influencing video popularity.

## Resources
- **GitHub Repository**: https://github.com/aurozsa/youtube_data_analysis
- **Additional Resources**: Articles and documentation on using the YouTube Data API.

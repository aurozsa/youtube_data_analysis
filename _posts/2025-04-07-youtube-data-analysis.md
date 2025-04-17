---
layout: post
title: "Exploring Engagement Metrics: Insights from YouTube's Trending Videos"
date: 2025-04-17
description: "Analysis of views, likes, and comments on YouTube trending music videos."
categories: [data-science, youtube-analytics]
image: "/assets/img/metrics_banner.jpg"
display_image: true
permalink: /youtube_data_analysis/2025/04/17/youtube-data-analysis.html
---

# Exploring Engagement Metrics: Insights from YouTube's Trending Music Videos

## Introduction
In today’s digital age, engagement metrics such as views, likes, and comments are crucial indicators of success for online content creators. These metrics not only measure a video's popularity but also help creators refine their strategies for reaching larger audiences. This analysis focuses on trending music videos on YouTube to explore how these engagement metrics evolve during the initial weeks following a video’s release. Our motivating question is: What is the relationship between the popularity of trending music videos and engagement metrics (views, likes, comments) over time?

To further empower data enthusiasts and creators, an interactive Streamlit app accompanies this analysis. The app enables users to explore the dataset and generate insights dynamically.

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
- Category ID and Category Name

### Ethics
Care was taken to ensure compliance with YouTube’s terms of service. Data collected did not include private or sensitive information, and only publicly available metrics were accessed and analyzed.

### Collection Process
- A Python script was used to query the YouTube Data API.
- Parameters such as "mostPopular" videos in the "Music" category were specified to refine the results.
- Data points like video title, channel name, views, likes, comments, publish date, trending date, and category information were extracted and saved into a CSV file.

## Data Exploration and Cleaning
### Initial Dataset
The raw dataset contained 200 records, each with eight features:
1. Video Title
2. Channel Name
3. Views
4. Likes
5. Comments
6. Publish Date
7. Trending Date
8. Category ID and Category Name

### Cleaning Steps
- **Handling Missing Values**: Missing values in the "likes" and "comments" columns were filled with 0.
- **Data Formatting**: Publish and trending dates were converted into a consistent format.
- **Deduplication**: Duplicate records were removed to ensure unique entries.
- **Category Mapping**: Category IDs were mapped to their respective category names for clarity in analysis.
- These steps ensured the dataset was ready for exploratory analysis.

## Exploratory Data Analysis
### Summary Statistics
Key descriptive statistics for the updated dataset:

| Metric           | Count     | Mean       | Std Dev      | Min     | 25%      | Median   | 75%      | Max        |
|------------------|-----------|------------|--------------|---------|----------|----------|----------|------------|
| **Views**        | 200       | 1,515,051  | 2,417,535    | 42,519  | 310,743  | 732,510  | 1,592,418| 19,745,440 |
| **Likes**        | 200       | 51,226     | 87,352       | 0       | 7,800    | 22,331   | 63,238   | 899,345    |
| **Comments**     | 200       | 4,512      | 8,759        | 74      | 872      | 1,905    | 4,215    | 79,860     |
| **Category ID**  | 200       | 18.54      | 6.19         | 1       | 17.0     | 20.0     | 24.0     | 28.0       |

### Visual Insights
#### **Average Views Over Time**
This time-series plot shows how average views change over the publish dates for trending videos:

![Time-Series Plot]({{site.url}}{{site.baseurl}}/assets/img/average_views_over_time.png)

#### **Distribution of Views**
The histogram below illustrates the distribution of views for the trending videos:

![Distribution Plot]({{site.url}}{{site.baseurl}}/assets/img/distribution_of_views.png)

#### **Correlation Matrix**
The heatmap below highlights the correlation between views, likes, and comments:

![Correlation Matrix]({{site.url}}{{site.baseurl}}/assets/img/correlation_matrix.png)

#### **Views by Category**
The boxplot below demonstrates the distribution of views across different video categories:

![Views by Category]({{site.url}}{{site.baseurl}}/assets/img/views_by_category_boxplot.png)

#### **Likes per View Distribution**
The histogram below highlights the distribution of the "likes per view" metric for videos:

![Likes per View Distribution]({{site.url}}{{site.baseurl}}/assets/img/likes_per_view_distribution.png)

### Findings
- Engagement tends to peak within the first week of a video trending.
- Videos in categories like "Music" and "Gaming" showed higher engagement metrics compared to others.
- Viral videos in the dataset have a much higher "likes per view" ratio, suggesting stronger audience impact.

---

## Interactive Exploration with Streamlit
In addition to this analysis, we’ve developed a Streamlit app that allows users to interact with the dataset dynamically. The app empowers users to uncover insights beyond those presented here. Key features include:

- **Dynamic Filters**: Explore videos by category, publish date, and engagement metrics.
- **Interactive Visualizations**: Generate customized time-series plots, correlation heatmaps, and category comparisons.
- **Engagement Analysis**: Investigate metrics like "likes per view" with adjustable thresholds.
- **Downloadable Data**: Save filtered datasets for offline analysis.

[Explore the Streamlit App Here](https://app-youtube-app-haqnwoytgjmehi5yyk3k6n.streamlit.app/)

This app provides a hands-on approach for analyzing YouTube's trending videos and discovering trends in engagement metrics.

---

## Conclusion
### Key Takeaways
This analysis highlights the importance of early engagement metrics in determining the overall success of YouTube music videos. Categories like Music and Gaming exhibit high levels of engagement, indicating their dominance on the trending page. The Streamlit app further enables users to perform in-depth data exploration to derive additional insights.

### Future Work
Potential future analyses could incorporate additional features, such as geographic data or video genres, to understand the broader factors influencing video popularity.

## Resources
- **GitHub Repository**: [YouTube Data Analysis](https://github.com/aurozsa/youtube_data_analysis)
- **Streamlit App**: [Interactive Data Exploration](link-to-app)
- **Additional Resources**: Articles and documentation on using the YouTube Data API.

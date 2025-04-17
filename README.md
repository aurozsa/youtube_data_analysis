# YouTube Data Analysis Blog

## Overview
This repository contains the project files for a comprehensive analysis of YouTube's trending videos, focusing on engagement metrics such as views, likes, comments, and derived features like "likes per view." The analysis explores key insights through a blog post, visualizations, and an interactive Streamlit app.

## Features
- **Exploratory Data Analysis (EDA)**: Python scripts to clean, explore, and visualize engagement data from YouTube.
- **Streamlit App**: An interactive tool for dynamic exploration of engagement metrics.
- **Blog Post**: A detailed write-up highlighting key insights, visualizations, and the app's functionality.
- **Visualizations**: PNG images of statistical plots, including time-series analysis, distributions, and boxplots.
  

## Instructions
### 1. Blog Post
The blog post can be found in `_posts/2025-04-07-youtube-data-analysis.md`. It includes key findings, visual insights, and links to the Streamlit app.

### 2. Streamlit App
The interactive Streamlit app is included in `youtube_data_analysis.py`. Follow these steps to run it:
1. Install the required Python libraries using:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the app:
    ```bash
    streamlit run executables/youtube_data_analysis.py
    ```
3. Access the app in your browser to explore the dataset dynamically.

### 3. Visualizations
All generated visualizations (PNG images) are stored in `assets/img/`.

### 4. Data Files
* `cleaned_youtube.data.csv`: The cleaned dataset extracted from the YouTube API.
* `cleaned_youtube_data_with_eda.csv`: An enriched dataset with additional EDA features such as "likes per view" and "comments per view."

### 5. GitHub Pages
The blog and its associated files are hosted using GitHub Pages. Access the blog via: `https://aurozsa.github.io/youtube_data_analysis`

### Requirements
The Python environment for running the scripts and Streamlit app requires:
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    plotly
Refer to `requirements.txt` for versions.

### Resources
* **GitHub Repository**: `https://github.com/aurozsa/youtube_data_analysis`
* **Streamlit App**: ` `

### Author
**Austin Rozsa** 
    Exploring data science and storytelling through YouTube trends and metrics.
# Article Scraper and Analysis

## Overview
This project is a web scraping and analysis tool that extracts news articles from Moneycontrol and performs NLP-based analysis using NLTK and Gemini LLM.

## Features
- Scrapes news article links from the Moneycontrol website.
- Extracts headlines, descriptions, and full content from each article.
- Saves extracted data into a JSON file.
- Performs NLP analysis using NLTK (tokenization, word frequency, sentiment analysis, etc.).
- Generates visual insights using Matplotlib and WordCloud.
- Provides LLM-based text summarization and insights using Gemini API.

## Installation

### Prerequisites
Ensure you have Python installed along with the required libraries:

```sh
pip install requests beautifulsoup4 nltk matplotlib wordcloud google-generativeai
```

## Usage

### 1. Run the Scraper
Execute the script to scrape articles and save them to `news_article.json`:

```sh
python main.py
```

### 2. Perform NLP Analysis
Run the analysis script to process and visualize the extracted data:

```sh
python analysis.py
```

### 3. Use LLM for Advanced Analysis
Execute the script to analyze articles using the Gemini API:

```sh
python llm_analysis.py
```

## File Structure
```
|-- article_scraper_analysis/
    |-- scraper.py           # Script to scrape articles
    |-- analysis.py          # NLP analysis script
    |-- llm_analysis.py      # LLM-based text analysis using Gemini
    |-- news_article.json    # Extracted news articles
    |-- README.md            # Project documentation
```

## Contributions
Feel free to fork this repository and contribute improvements via pull requests.

## License
This project is licensed under the MIT License.


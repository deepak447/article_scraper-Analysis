import json
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import PorterStemmer, WordNetLemmatizer

from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os


with open("news_article.json", "r") as file:
    data = json.load(file)


descriptions = [article["Description"] for article in data.values() if "Description" in article]

all_words = []
for desc in descriptions:
    words = word_tokenize(desc.lower())  # Convert to lowercase
    all_words.extend(words)

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in all_words if word.isalnum() and word not in stop_words]
# print("Sample Words After Stopword Removal:", filtered_words[:20])

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Lemmatization (Reducing words to base form)
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

sentiment_results = {}
for i, desc in enumerate(descriptions[:5]):  # Analyzing first 5 descriptions
    sentiment = sia.polarity_scores(desc)
    sentiment_results[f"description_{i+1}"] = {
        "text": desc,
        "sentiment": sentiment
    }

# Save the sentiment results to a JSON file
with open("nltk_analysis.json", "w") as json_file:
    json.dump(sentiment_results, json_file, indent=4)

print("Sentiment analysis saved in nltk_analysis.json")




# Define folder and file path
output_folder = "wordcloud_images"
os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

file_path = os.path.join(output_folder, "wordcloud.png")

# Generate word cloud from lemmatized words
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(lemmatized_words))

# Save the word cloud image
wordcloud.to_file(file_path)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

print(f"Word cloud saved at: {file_path}")

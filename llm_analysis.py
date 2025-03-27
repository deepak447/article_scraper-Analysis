import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv
import json

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

with open("news_article.json", "r") as file:
    data = json.load(file)

def analyze_text_with_gemini(text):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  

    prompt = f"""
    Analyze the following news content:
    
    1. Extract key topics.
    2. Perform sentiment analysis (Positive, Neutral, Negative).
    3. Provide a short summary.
    
    News content: {text}
    """

    response = model.generate_content(prompt)
    return response.text

content = [article["Content"] for article in data.values() if "Content" in article]

llm_results = {}

# Load existing data if the file already exists
if os.path.exists("llm_analysis.json"):
    with open("llm_analysis.json", "r") as file:
        llm_results = json.load(file)

# Analyze first 3 news contents and store results
for i, cont in enumerate(content[:3]):  
    analysis = analyze_text_with_gemini(cont)
    llm_results[f"news_{i+1}"] = {
        "text": cont,
        "analysis": analysis
    }

# Save the updated analysis results to the JSON file
with open("llm_analysis.json", "w") as json_file:
    json.dump(llm_results, json_file, indent=4)

print("LLM analysis saved in llm_analysis.json")
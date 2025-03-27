from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
import os
import json

from article import extract_news


base_url = "https://www.moneycontrol.com/news/business/companies/"
headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

def extract_links(base_url, headers):
    """
    Extracts news article links from the given website, fetches the news content,
    and saves it in a JSON file.

    Args:
        base_url (str): The URL of the website from which news links will be extracted.
        headers (dict): The headers to use for the HTTP request.

    Returns:
        dict: A dictionary with a success message confirming that articles were saved.
    """
    articles_dict = {}
    response = requests.get(base_url, headers = headers)
    soup = BeautifulSoup(response.content,"html.parser") 
    urls = soup.find_all("div",{'class':'fleft'}) 
    link_list = []
    for s in urls:
        h2_tags = s.find_all('h2')  
    
        for h in h2_tags:
        # Check if the current <h2> tag has a premium indicator
            if h.find('span', class_='isPremiumCrown'):  
                continue  # Skip premium articles

            a_tag = h.find('a') 
            if a_tag and a_tag.get('href'):  
                links = a_tag['href'] 
                if links not in articles_dict:
                    articles_dict[links] = extract_news(links, headers)

    if os.path.exists("news_article.json"):
        with open("query_categories.json", "r") as file:
            data_dict = json.load(file)
    else:
        data_dict = {}
         
    data_dict.update(articles_dict)
    with open("news_article.json", "w") as json_file:
        json.dump(data_dict, json_file, indent=4)
                
    return {
        'message':"articles saved in file"
    }
        

if __name__ == "__main__":
    result = extract_links(base_url, headers)
    print(result)


    


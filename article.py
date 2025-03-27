import requests
from bs4 import BeautifulSoup


def extract_news(url,headers):
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.text, 'html.parser')
    headline = soup.find('h1',{'class':'article_title artTitle'}).text.strip()
    description = soup.find('h2',{'class':'article_desc'}).text.strip()
    article_ = soup.find('div',{'class':'page_left_wrapper'})
    ids = article_.find('div',{'id':'contentdata'})
    p_tag = ids.find_all('p')

    contents = ""
    for p in p_tag:
        content = p.text.strip()
        contents += content + " "
        # print(content_list)
    articles = {
         "Headline" : headline,
         'Description' : description,
         'Content' : contents
     }   
    return articles
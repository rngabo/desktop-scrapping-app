import requests
from bs4 import BeautifulSoup
import time

def get_bbc_news():
    url = "https://www.bbc.com/news/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    news_headline_elements = soup.find('div', id='news-top-stories-container').find('a').find('h3')
    
    if news_headline_elements:
        news_headline = news_headline_elements.text
        return f"BBC: {news_headline}"
    else:
        return "BBC: News headline not found."

def get_techcrunch_news():
    url = "https://techcrunch.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    news_headline_element = soup.find("a", class_="post-block__title__link")

    if news_headline_element:
        news_headline = news_headline_element.text
        return f"TechCrunch: {news_headline}"
    else:
        return "TechCrunch: News headline not found."

def print_news():
    bbc_news = get_bbc_news()
    techcrunch_news = get_techcrunch_news()
    return f"\n{bbc_news}\n\n{techcrunch_news}"

time.sleep(35)
print(print_news())

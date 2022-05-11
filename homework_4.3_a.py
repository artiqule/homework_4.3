import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru'

def scraping_preview():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all('article')
    for article in articles:
        dates = article.text.lower().split(' ')
        for word in KEYWORDS:
            if word in dates:
                date = article.find(class_="tm-article-snippet__datetime-published").time.get('title')
                header = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
                link = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2")
                link = URL[:-3] + link.a.get('href')
                print(f'Дата: {date} -- Заголовок: {header} -- Ссылка: {link}')


scraping_preview()
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

news_list = soup.findAll('article', class_='tm-articles-list__item')

links = []
for news in news_list:
    time = news.find('span', class_='tm-article-snippet__datetime-published').text
    name = news.find('a', class_='tm-article-snippet__title-link').text
    link = "https://habr.com" + news.find('a', class_='tm-article-snippet__title-link').get('href')
    links.append(link)
    for i in KEYWORDS:
        if i in name:
            print(f'Дата: {time} - Заголовок: {name} - Ссылка: {link} \n')

counter = 0
for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')
    article = soup.find('article', class_='tm-article-presenter__content tm-article-presenter__content_narrow').find('div', class_='tm-article-body').text
    for i in KEYWORDS:
        if i in article:
            counter += 1
            print(f'Статья № {counter} \n {link} \n')

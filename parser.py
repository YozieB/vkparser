import requests
from bs4 import BeautifulSoup as BS


# Логика парсинга

URL = 'https://m.vk.com/artist/maywaves'

HEADERS = (
    {'user-agent':
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     '(KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
)
HOST = 'https://m.vk.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='audioPlaylistsPage__cell_link')

    release_info = []

    for item in items:
        release_info.append({
            'title':
            item.find('span', class_='audioPlaylistsPage__title').get_text(),
            'author':
            item.find('span', class_='audioPlaylistsPage__author').get_text(),
            'year':
            item.find('span', class_='audioPlaylistsPage__stats').get_text(),
            'link':
            HOST + item.find('a', class_='audioPlaylistsPage__itemLink')
            .get('href'),
        })

    return release_info

# Основная функция парсинга


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Что-то пошло не так(')


parse()

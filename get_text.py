import re
import feedparser
from nltk import sent_tokenize


def clear(text):
        while re.findall(r'<[^>]+>', text):
            text = re.sub(r'<[^>]+>', ' ', text)

        while re.findall(r'&laquo;', text):
            text = re.sub(r'&laquo;', ' ', text)

        while re.findall(r'&raquo;', text):
            text = re.sub(r'&raquo;', ' ', text)

        while re.findall(r'&nbsp;', text):
            text = re.sub(r'&nbsp;', ' ', text)

        return text


def get_text(url, path):
        NewsFeed = feedparser.parse(url)
        i = 0
        for entry in NewsFeed.entries:
            entry = NewsFeed.entries[i]
            f = open(path + '\\' + str(i + 1) + '.txt', 'w', encoding='utf-8')
            f.write(clear(entry['yandex_full-text']))
            f.close()
            i += 1


urls = {'http://vesti.ru/vesti.rss',
        'http://www.aif.ru/rss/news.php',
        'http://gnkk.ru/news/rss/',
        'https://dni24.com/rss.xml',
        'https://x-true.info/novosti/rss.xml',
        'http://www.kurer-sreda.ru/wp-yandex.php',
        'http://www.infox.ru/themes/hi-tech/rss.xml',
        'http://www.vz.ru/export/yandex.xml',
        'http://svpressa.ru/xml/news.xml',
}

path = 'Эксперимент\\'
get_text('http://vesti.ru/vesti.rss', path)



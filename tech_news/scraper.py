import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response_url = requests.get(
            url,
            headers={'user-agent': 'Fake user-agent'},
            timeout=3
        )
        if (response_url.status_code != 200):
            return None
    except requests.ReadTimeout:
        return None
    else:
        return response_url.text


# Requisito 2
def scrape_updates(html_content):
    if (not html_content):
        return []
    html = Selector(text=html_content)
    list_links = html.css('h2.entry-title a::attr(href)').getall()
    return list_links


# Requisito 3
def scrape_next_page_link(html_content):
    html = Selector(text=html_content)
    link_next = html.css('a.next::attr(href)').get()
    if (not link_next):
        return None
    return link_next


# Requisito 4
def scrape_news(html_content):
    html = Selector(text=html_content)
    dict_news = {
        'url': html.css('head link[rel="canonical"]::attr(href)').get(),
        'title': html.css('.entry-title::text').get().strip(),
        'timestamp': html.css('li.meta-date::text').get(),
        'writer': html.css('span.author a::text').get(),
        'reading_time': int(html.css('.meta-reading-time::text').get()[0:2]),
        'summary': ''.join(
            html.css('.entry-content > p:first-of-type *::text')
            .getall()).strip(),
        'category': html.css('.label::text').get(),
    }
    return dict_news


# Requisito 5
def get_tech_news(amount):
    list_news = []
    page = 'https://blog.betrybe.com/'
    while len(list_news) < amount:
        response_fetch = fetch(page)
        response_links = scrape_updates(response_fetch)
        for res in response_links:
            response_news = fetch(res)
            list_news.append(scrape_news(response_news))
        page = scrape_next_page_link(response_fetch)
    create_news(list_news[0:amount])
    return list_news[0:amount]

import requests
import time
from parsel import Selector


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
    response_fetch = fetch(html_content)
    html_selector = Selector(text=response_fetch)
    list_links = html_selector.css('a.url::attr(href)').getall()
    return list_links[1:]


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
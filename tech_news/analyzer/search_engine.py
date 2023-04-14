from tech_news.database import db


# Requisito 7
def search_by_title(title):
    list_title = []
    search = db.news.find(
        {'title': {'$regex': title, '$options': 'i'}}
    )
    for value in search:
        list_title.append((value['title'], value['url']))
    return list_title


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

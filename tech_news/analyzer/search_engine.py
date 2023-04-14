from tech_news.database import db
from datetime import datetime


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
    try:
        date_find = datetime.fromisoformat(date)
    except ValueError:
        raise ValueError('Data inválida')
    else:
        list_title = []
        search = db.news.find(
            {'timestamp': format(date_find, '%d/%m/%Y')}
        )
        for value in search:
            list_title.append((value['title'], value['url']))
        return list_title


# Requisito 9
def search_by_category(category):
    list_title = []
    search = db.news.find(
        {'category': {'$regex': category, '$options': 'i'}}
    )
    for value in search:
        list_title.append((value['title'], value['url']))
    return list_title

from operator import itemgetter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    ranking = {}
    for news in find_news():
        if (not news['category'] in ranking):
            ranking[news['category']] = 1
        else:
            ranking[news['category']] += 1
    list_tuples = list(ranking.items())
    list_tuples.sort(key=itemgetter(0))
    list_result = sorted(list_tuples, key=itemgetter(1), reverse=True)
    list_ranking = [value[0] for value in list_result]
    return list_ranking[:5]

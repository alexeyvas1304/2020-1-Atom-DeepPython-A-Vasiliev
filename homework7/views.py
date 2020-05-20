import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from collections import Counter
import json
from stop_words import stop_words
from http_response import HttpResponse


def get_top_words(request):
    url = request  # так привычнее
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
    except MissingSchema:
        print('Bad url - no schema')
        return HttpResponse(status_code=404, data=json.dumps({'Failed': 'bad request'}))
    except requests.exceptions.InvalidURL:
        print('Bad url')
        return HttpResponse(status_code=404, data=json.dumps({'Failed': 'bad request'}))
    except requests.exceptions.ConnectionError:
        print('Bad url')
        return HttpResponse(status_code=404, data=json.dumps({'Failed': 'bad request'}))

    soup = BeautifulSoup(r.text, 'html.parser')
    lst_of_words = soup.get_text().split()
    lst_cleared_1_stage = list(map(lambda x: x.strip('()/.,!?<>=;:').lower(), lst_of_words))
    lst_cleared_2_stage = list(filter(lambda x: len(x) > 1 and x not in stop_words, lst_cleared_1_stage))
    dict_of_popular_words = dict(Counter(lst_cleared_2_stage).most_common(10))
    response = json.dumps(dict_of_popular_words, ensure_ascii=False)
    return HttpResponse(data=response)

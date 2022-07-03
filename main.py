import time
import requests
import datetime
from pprint import pprint
import ya_disk


def best_intelligence_stats():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    result = {}
    for hero in response.json():
        if hero['name'] in heroes_list:
            result[hero['name']] = hero['powerstats']['intelligence']
    best_intelligence = max(result.items(), key=lambda x: x[1])
    return f'Самый умный супергерой - {best_intelligence[0]}'


def stackoverflow_questions_list(tag: str):
    now = datetime.datetime.now()
    fromdate = int(time.mktime((now - datetime.timedelta(days=2)).timetuple()))
    todate = int(time.mktime(now.timetuple()))
    params = {'fromdate': fromdate,
              'todate': todate,
              'tagged': tag,
              'order': 'desc',
              'sort': 'activity',
              'site': 'stackoverflow'}
    url = 'https://api.stackexchange.com/2.3/questions'
    result = requests.get(url=url, params=params).json()
    return result



if __name__ == '__main__':
    # Задача №1
    print(best_intelligence_stats())
    # Задача №2
    TOKEN = ''
    ya = ya_disk.Yandex(token=TOKEN)
    ya.upload_file(file_path='test.txt', filename='files_to_upload/test.txt')
    # Задача №3
    pprint(stackoverflow_questions_list('Python'))
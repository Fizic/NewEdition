import requests
from bs4 import BeautifulSoup as BS
import random

data = {}


def take_game_data(link):
    req = requests.get(link)
    html = BS(req.content, 'html.parser')

    # Getting teams names
    teams = html.select('.b-flag')
    team_1 = str(teams[0]).split('alt')[1][
             2:str(teams[0]).split('alt')[1].index('src') - 2]
    team_2 = str(teams[1]).split('alt')[1][
             2:str(teams[1]).split('alt')[1].index('src') - 2]

    # Getting 1-team points
    h = str(html.select('.b-score_first')[0])
    score_1 = h.split('>')[1][:h.split('>')[1].index('<')]

    # Getting 2-team points
    h = str(html.select('.b-score_second')[0])
    score_2 = h.split('>')[1][:h.split('>')[1].index('<')]

    return team_1, team_2, score_1, score_2


def random_match_result():
    r = requests.get('https://www.sport-express.ru/live/yesterday/')
    html = BS(r.content, 'html.parser')
    raw_matches = html.select('.se19-translation-block__link')

    matches = []
    for match in raw_matches:
        match = str(match).split('href')[1][2:str(match).split('href')[1].index('>') - 1]
        matches.append(match)

    return take_game_data(matches[random.randint(0, len(matches) - 1)])


def creating_text():
    data = random_match_result()
    titles = [f'Команда {data[0]} победила {data[1]} со счетом {data[2]}:{data[3]}',
              f'{data[0]} разгромила {data[1]} со счетом {data[2]}:{data[3]}']
    descriptions = [f'Хоть этот матч и не войдет в историю, но о нем стоит узнать',
                    'Мы думаем этот матч стоит посмотреть']
    imgs = ['https://static.make.ua/catalog/13/sport-0000126__1399387745__615.jpg',
            'https://static8.depositphotos.com/1447017/924/i/450/depositphotos_9246448-stock-photo-football-the-ball-flies-into.jpg']
    return random.choice(titles), random.choice(descriptions), random.choice(imgs)


def creating_voc():
    data = creating_text()
    info = {
        'title': data[0],
        'description': data[1],
        'img': data[2],
    }
    return info

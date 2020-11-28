import requests


def take_data():
    key_api = ''
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + key_api
    city = 'London'
    data = requests.get(url.format('london')).json()
    return data


print(take_data())

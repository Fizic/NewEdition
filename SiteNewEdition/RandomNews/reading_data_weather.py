import requests


def take_data():
    key_api = '08ae9239449049aed5d6d40d9b9ad307'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + key_api
    city = 'London'
    data = requests.get(url.format('london')).json()
    return data


print(take_data())

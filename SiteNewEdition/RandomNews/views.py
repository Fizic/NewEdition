from django.shortcuts import render
from . import reading_data_football
import requests
import random


def index(request):
    kinds_news = []
    context = {'all_info': []}

    for _ in range(random.randint(1, 15)):
        context['all_info'].append(reading_data_football.creating_voc())

    return render(request, 'RandomNews/index.html', context)
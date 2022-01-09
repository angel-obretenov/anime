import requests
from django.shortcuts import render

from utils.query_checker import get_allowed_queries
from utils.ratings import calculate_ratings, get_anime_rating_percentage
from .jikanApi.jikanapi import JikanApi

api = JikanApi()


def anime_search(request):
    queries = {}
    if request.method == 'POST':
        queries["q"] = request.POST.get('anime-searched')
    else:
        queries = get_allowed_queries(request.GET)

    data = api.search_anime(queries)

    context = {}
    if not data.get("error") and data.get('results'):
        context['data'] = data["results"]
        context['last_page'] = data["last_page"]
        ratings = calculate_ratings([anime['score'] for anime in data["results"]])
        
        context['labels'] = ratings.keys()
        context['values'] = ratings.values()

    return render(request, 'index.html', context)


def anime_detailed(request, pk):
    data = api.get_detailed_anime(pk)

    context = {}
    if not data.get("error"):
        context['data'] = data
        context['liked'], context['disliked'] = get_anime_rating_percentage(data['score'])

    return render(request, 'anime_detail.html', context)

import json
import requests


class JikanApi(object):
    def __init__(self):
        self.URL = 'https://api.jikan.moe/v3/'

    def search_anime(self, queries: dict):
        data = requests.get(self.URL + f'search/anime', params=queries)

        return data.json()

    def get_detailed_anime(self, anime_id: str):
        data = requests.get(self.URL + f'anime/{anime_id}/')

        return data.json()

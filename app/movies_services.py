


import requests
from passwords import API_TOKEN
from app.utilities import remove_empty_item


BASE_URL = "https://api.themoviedb.org/3/"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_now_playing(region="BG"):
    
    
    
    params = {
        "region": region
    }
    
    
    url = BASE_URL + "movie/now_playing"
    
    
    response =  requests.get(url,headers=HEADERS, params=params)
    
    
    json_data = response.json()
    
    now_playing_movies = json_data["results"]
    
    return now_playing_movies
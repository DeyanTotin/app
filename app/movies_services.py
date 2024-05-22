


import requests
from passwords import API_TOKEN
from app.utilities import remove_empty_item


BASE_URL = "https://api.themoviedb.org/3/"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_now_playing(region="US", page=1):
    
    
    
    params = {
        "region": region,
        "page": page
    }
    
    
    url = BASE_URL + "movie/now_playing"
    
    
    response =  requests.get(url,headers=HEADERS, params=params)
    
    
    json_data = response.json()
    
    now_playing_movies = json_data["results"]
    
    return remove_empty_item(now_playing_movies)



def get_movie_by_id(id):
    id = int(id)
    
    url = BASE_URL + f"movie/{id}"
    
    
    response = requests.get(url, headers=HEADERS)
    json_repsonse = response.json()
    return json_repsonse
    
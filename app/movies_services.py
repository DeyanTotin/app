

import requests
from passwords import API_TOKEN

BASE_URL = "https://api.themoviedb.org/3/"




def get_movies(movie_title: str):
    
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    
    params = {
        
        "query": movie_title,
        "include_adult": True,
        "language": "en-US",
        "page": 1,
        "region": None
            
    }
    
    url = BASE_URL + "search/collection"
    
    response = requests.get(url, headers=headers, params=params)
   
    json_response = response.json() 
    
  
    movies = []
    
    
    if "Error" in json_response:
        return []
    if "results" in json_response:    
        movies = json_response["results"]

        return movies
        
        
  
        
   



import requests
from passwords import API_KEY

URL = "http://www.omdbapi.com/"




def get_movies(movie_title: str):
    
    params = {
        "apikey": API_KEY,
        "s": movie_title,
            
    }
    
    response = requests.get(URL, params=params)
   
    json_response = response.json() 
    
  
    movies = []
    
    if "Error" in json_response:
        return []
    if "Search" in json_response:    
        movies = json_response["Search"]

        return movies
        
        
  
        
   

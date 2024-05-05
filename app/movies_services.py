
import json
import requests
from passwords import API_KEY

URL = "http://www.omdbapi.com/"




def get_movie_by_title(movie_title: str):
    
    params = {
        "apikey": API_KEY,
        "t": movie_title
        
    }
    
    response = requests.get(URL, params=params)
    json_data = json.loads(response.text)

    return json_data





import requests
from passwords import API_TOKEN


BASE_URL = "https://api.themoviedb.org/3/"




def get_collections(collection_title: str):
    
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    
    params = {
        
        "query": collection_title,
        "include_adult": True,
        "language": "en-US",
        "region": None
            
    }
    
    url = BASE_URL + "search/collection"
    
    response = requests.get(url, headers=headers, params=params)
   
    json_response = response.json() 
    
  
    
    if "results" in json_response:    
        collections = json_response["results"]
     
        return collections
        
        
  

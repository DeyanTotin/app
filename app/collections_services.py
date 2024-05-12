

import requests
from passwords import API_TOKEN
from app.utilities import remove_empty_item

BASE_URL = "https://api.themoviedb.org/3/"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_collections(collection_title: str):
    
    
    params = {
        
        "query": collection_title,
        "include_adult": True,
        "language": "en-US",
        "region": None
            
    }
    
    url = BASE_URL + "search/collection"
    
    response = requests.get(url, headers=HEADERS, params=params)
   
    json_response = response.json() 
    
  
    
    if "results" in json_response:    
        collections = json_response["results"]

     
     
        return remove_empty_item(collections)
        
        
  
def get_collection_by_id(id):
    
    id = int(id)
    
    
    url = BASE_URL + f"collection/{id}"
    
    response = requests.get(url, headers=HEADERS)
    
    json_respone = response.json()
    print(json_respone)
    
    
    return json_respone
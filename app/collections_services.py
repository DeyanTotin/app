

import requests
# from passwords import API_TOKEN

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmN2M4MGFmMmY4NDI3ZmU4OTAwMWIyNzE5ZGVhNTU4YSIsInN1YiI6IjY2Mzc1ZTY1MzU4ZGE3MDEyYTU2NjA2MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kGdh3QivdUl2CUNBIRjTYExwhjz1MNlW5gFeMPN2gyA"

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
        
        
  

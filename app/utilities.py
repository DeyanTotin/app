


def remove_empty_item(items: list):


    for item in items[:]:
        
        if not item["overview"]:
            items.remove(item)
        elif item["poster_path"] is None:
            items.remove(item)
        
    return items    
    
    
            
        
        
        
        
         
    
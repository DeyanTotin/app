
from flask import Flask, request, render_template
from app.collections_services import get_collections

app = Flask(__name__)



@app.route("/collections", methods = ["GET"])
def search_collections():
    if request.method == "GET":
        
        collection_title = request.args.get("content", "").strip()
        
        

        if collection_title:
   
            collections = get_collections(collection_title)
            total_results = len(collection_title)
             
            
        else:
            collections = []
            total_results = 0
        return render_template("index.html", collections=collections, total_results=total_results)

    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
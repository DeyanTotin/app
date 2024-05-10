
from flask import Flask, request, render_template
from app.collections_services import get_collections

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home_page():
    
    return render_template("index.html")


@app.route("/collections", methods = ["GET"])
def search_collections():
    if request.method == "GET":
        
        collection_title = request.args.get("content", "").strip()
        
        

        if collection_title:
   
            collections = get_collections(collection_title)
            
             
            
        else:
            collections = []
            
            
            
        chunks = [collections[i:i + 4] for i in range(0, len(collections), 4)]
        
        return render_template("collections.html", chunks=chunks)

    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
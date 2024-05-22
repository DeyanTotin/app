
from flask import Flask, request, render_template
from app.collections_services import get_collections, get_collection_by_id
from app.movies_services import get_now_playing, get_movie_by_id
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "GET":
        

        
        return render_template("index.html")

@app.route("/movies", methods = ["GET", "POST"])
def search_movies():
        if request.method == "GET":
            
            
            page = int(request.args.get("page",1))
            if page < 1:
                page =1
            
            print(page)
        
            now_playing = get_now_playing(page=page)
            chunks = [now_playing[i:i + 4] for i in range(0, len(now_playing), 4)]
            
            return render_template("movies.html", chunks=chunks, page=page)


@app.route("/movie/<id>", methods=["GET"])
def get_movie(id):
    if request.method == "GET":
        movie = get_movie_by_id(id)
        
        return render_template("movie.html", movie=movie)


@app.route("/tvs", methods = ["GET", "POST"])
def search_tvs():
    return render_template("tvs.html")


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

    
@app.route("/collection/<id>", methods=["GET"])
def get_collection(id):
    
    if request.method == "GET":
        collection = get_collection_by_id(id)
        
        return render_template("collection.html", collection=collection)
        
        
        
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
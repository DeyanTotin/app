
from flask import Flask, request, render_template
from app.movies_services import get_movies

app = Flask(__name__)



@app.route("/", methods = ["GET"])
def search_movie():
    if request.method == "GET":
        
        movie_title = request.args.get("content", "").strip()
        total_movies = 0
        if movie_title:
            
            movies = get_movies(movie_title)
            total_movies = len(movies)
            
        else:
            movies = []

        return render_template("index.html", movies=movies, total_movies=total_movies)

    
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
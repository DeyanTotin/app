
from flask import Flask, request
from app.movies_services import get_movie_by_title

app = Flask(__name__)



@app.route("/")
def home_page():
    return "<p>This is the home page<p/>"


@app.route("/search/<string:movie_title>", methods = ["GET"])
def search_movie(movie_title: str):
    if request.method == "GET":
        data = get_movie_by_title(movie_title)
        
        return f"<p>{data}</p>"
    
    
    
    
    
    
    






if __name__ == "__main__":
    app.run(debug=True)
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

#
# Listado de películas de ejemplo
#

dbmovies = [
        {
        "id":1,
        "title":"Avatar",
        "overview":"En un exuberante planeta llamado pandora",
        "year":"2009",
        "rating":7.8,
        "category":"Accion"
        },
        {
        "id":2,
        "title":"Avenger",
        "overview":"Ante la amenaza de un terrible dictador galactico...",
        "year":"2004",
        "rating":6.7,
        "category":"Accion"
        }
        ]

@app.get('/', tags=['Home'])
def message():
    return "Hello World!"

@app.get('/movies', tags=['Movies'])
def get_movies():
    return dbmovies 

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for movie in dbmovies:
        if movie['id'] == id:
            return movie
    return []

@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int):
    for movie in dbmovies:
        if movie['category'] == category:
            return movie
    return []


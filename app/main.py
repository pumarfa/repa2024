from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

class Movie (BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

class MovieUpdate (BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str
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
def get_movies()->List[Movie]:
    return dbmovies 

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int)-> Movie:
    for movie in dbmovies:
        if movie['id'] == id:
            return movie
    return []

@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int)->Movie:
    for movie in dbmovies:
        if movie['category'] == category:
            return movie
    return []

# Clase 8
@app.post('/movies', tags=['Movies'])
def create_movie(movie:Movie)->List[Movie]:
    dbmovies.append(movie.model_dump())
    return dbmovies 

# clase 9 - Método PUT y DELETE
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie:MovieUpdate)->List[Movie]:
    for item in dbmovies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview 
            item['year'] = movie.year 
            item['rating'] = movie.rating 
            item['category'] = movie.category 

    return dbmovies        
    
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int )->Movie:
    for movie in dbmovies:
        if movie['id'] == id:
            dbmovies.remove(movie)
    return dbmovies 



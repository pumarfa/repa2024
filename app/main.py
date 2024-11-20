from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List

import datetime 

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

class MovieCreate (BaseModel):
    id: int
    title: str =Field(min_length=5, max_length=15)
    overview: str = Field(min_length=0, max_length=150)
    year: int = Field(ge=1900, le=datetime.date.today().year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=0, max_length=30)

    model_config = {
        'json_schema_extra':{
            'example':{
                'id':0,
                'title':'My Movie',
                'overview':'Esta es un apelícula de ...',
                'year': 1900,
                'rating': 1.0,
                'category':'Drama'
                }
            }
        }

class MovieUpdate (BaseModel):
    title: str =Field(min_length=5, max_length=15)
    overview: str = Field(min_length=0, max_length=150)
    year: int = Field(ge=1900, le=datetime.date.today().year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=0, max_length=30)

#
# Listado de películas de ejemplo
#

dbmovies: List[Movie] = []

@app.get('/', tags=['Home'])
def message():
    return "Hello World!"

#
# Obtener un objeto con todas las películas
#
@app.get('/movies', tags=['Movies'])
def get_movies()->List[Movie]:
    return [movie.model_dump() for movie in dbmovies ] 

#
# Obtener un objeto con una pelicula por su ID
#
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int)-> Movie:
    for movie in dbmovies:
        if movie['id'] == id:
            return movie.model_dump
    return []

#
# Obtener una objeto con una película por su categoria
#
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int)->Movie:
    for movie in dbmovies:
        if movie['category'] == category:
            return movie.model_dump
    return []

# Clase 8
# Crear un objeto pelicula e insertarlo en la base de datos
#
@app.post('/movies', tags=['Movies'])
def create_movie(movie:MovieCreate)->List[Movie]:
    dbmovies.append(movie)
    return [ movie.model_dump() for movie in dbmovies ] 

# clase 9 - Método PUT y DELETE
# Crear un objeto película, buscar y reemplazar en la base de datos
#
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie:MovieUpdate)->List[Movie]:
    for item in dbmovies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview 
            item['year'] = movie.year 
            item['rating'] = movie.rating 
            item['category'] = movie.category 
    return [movie.model_dump() for movie in dbmovies ] 

#
# Buscar un objeto película en la base de datos y borrrlo
#
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int )->Movie:
    for movie in dbmovies:
        if movie['id'] == id:
            dbmovies.remove(movie)
    return [movie.model_dump() for movie in dbmovies ] 



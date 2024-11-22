from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field, validator
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
    title: str 
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
    @validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('Title field must have a minimun of 5 characters')
        if len(value) > 15:
            raise ValueError('Title field must have a maximun of 15 characters')
        return(value)

class MovieUpdate (BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str

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
@app.get('/movies', tags=['Movies'], status_code=200, response_description='Successful Response...')
def get_movies()->List[Movie]:
    content = [movie.model_dump() for movie in dbmovies ] 
    return JSONResponse(content = content, status_code=200)

#
# Obtener un objeto con una pelicula por su ID
#
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int= Path(ge=0))-> Movie | dict:
    for movie in dbmovies:
        if movie.id == id:
            return JSONResponse(content = movie.model_dump(), status_code=200)
    return JSONResponse(content = {}, status_code=404)

#
# Obtener una objeto con una película por su categoria
#
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str= Query(min_length=0, max_length=30))-> Movie | dict:
    for movie in dbmovies:
        if movie.category == category:
            return JSONResponse(content =movie.model_dump(), status_code=200)
    return JSONResponse(content = {}, status_code=404)

# Clase 8
# Crear un objeto pelicula e insertarlo en la base de datos
#
@app.post('/movies', tags=['Movies'])
def create_movie(movie:MovieCreate)->List[Movie]:
    dbmovies.append(movie)
    content = [ movie.model_dump() for movie in dbmovies ] 
    return JSONResponse(content = content, status_code=201)

# clase 9 - Método PUT y DELETE
# Crear un objeto película, buscar y reemplazar en la base de datos
#
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie:MovieUpdate)->List[Movie]:
    for item in dbmovies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview 
            item.year = movie.year 
            item.rating = movie.rating 
            item.category = movie.category 
    content = [movie.model_dump() for movie in dbmovies ] 
    return JSONResponse(content = content, status_code=200)

#
# Buscar un objeto película en la base de datos y borrrlo
#
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int=Path(ge=0) )->Movie:
    for movie in dbmovies:
        if movie.id == id:
            dbmovies.remove(movie)
    content = [movie.model_dump() for movie in dbmovies ] 
    return JSONResponse(content = content, status_code=200)




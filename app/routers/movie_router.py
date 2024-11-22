from typing import List
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from app.models.movie_model import Movie, MovieCreate, MovieUpdate

#
# Listado de películas de ejemplo
#

dbmovies: List[Movie] = []

movie_router = APIRouter()

#
# Obtener un objeto con todas las películas
#
@movie_router.get('/', tags=['Movies'], status_code=200, response_description='Successful Response...')
def get_movies()->List[Movie]:
    content = [movie.model_dump() for movie in dbmovies ]
    return JSONResponse(content = content, status_code=200)

#
# Obtener un objeto con una pelicula por su ID
#
@movie_router.get('/{id}', tags=['Movies'])
def get_movie(id: int= Path(ge=0))-> Movie | dict:
    for movie in dbmovies:
        if movie.id == id:
            return JSONResponse(content = movie.model_dump(), status_code=200)
    return JSONResponse(content = {}, status_code=404)

#
# Obtener una objeto con una película por su categoria
#
@movie_router.get('/by_category', tags=['Movies'])
def get_movie_by_category(category: str= Query(min_length=0, max_length=30))-> Movie | dict:
    for movie in dbmovies:
        if movie.category == category:
            return JSONResponse(content =movie.model_dump(), status_code=200)
    return JSONResponse(content = {}, status_code=404)

# Clase 8
# Crear un objeto pelicula e insertarlo en la base de datos
#
@movie_router.post('/', tags=['Movies'])
def create_movie(movie:MovieCreate)->List[Movie]:
    dbmovies.append(movie)
    content = [ movie.model_dump() for movie in dbmovies ]
    return JSONResponse(content = content, status_code=201)

# clase 9 - Método PUT y DELETE
# Crear un objeto película, buscar y reemplazar en la base de datos
#
@movie_router.put('/{id}', tags=['Movies'])
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
@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie(id: int=Path(ge=0) )->Movie:
    for movie in dbmovies:
        if movie.id == id:
            dbmovies.remove(movie)
    content = [movie.model_dump() for movie in dbmovies ]
    return JSONResponse(content = content, status_code=200)

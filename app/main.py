from fastapi import FastAPI, Body
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

# Clase 8
@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    dbmovies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating":rating,
        "category":category 
        })
    
    return dbmovies 

# clase 9 - Método PUT y DELETE
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for movie in dbmovies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview 
            movie['year'] = year 
            movie['rating'] = rating 
            movie['category'] = category 

    return dbmovies        
    
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int ):
    for movie in dbmovies:
        if movie['id'] == id:
            dbmovies.remove(movie)
    return dbmovies 



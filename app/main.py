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
        }
        ]

@app.get('/', tags=['Home'])
def message():
    return "Hello World!"

@app.get('/movies', tags=['Movies'])
def movies():
    return dbmovies 


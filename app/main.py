from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from app.routers.movie_router import movie_router

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

app.include_router(prefix='/movies', router=movie_router)

@app.get('/', tags=['Home'])
def message():
    return "Hello World!"

from pydantic import BaseModel, Field, validator
import datetime

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

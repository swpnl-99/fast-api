from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return { 
        "data": {
            "name": "Swapnil"
        }
    }

@app.get('/blog')
def index(limit:int = 10, published:bool = True , sort:Optional[str] = None):
    if published:
        return {'data': f"{limit} published blogs"}
    else:
        return {'data': f"{limit} blogs from db"}

@app.get('/about')
def about():
    return{
        "data": "about page"
    }

@app.get('/about/{id}')
def about(id : int):
    return{
        "data": id
    }

class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post('/post')
def create_blog(request : Blog):
    # return request
    return {'data':f'blog is created with {request.title}'}

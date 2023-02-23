from fastapi import FastAPI
from enum import Enum
from typing import Optional

# we use this line to start our server and to define our path(@app.get)
app = FastAPI()

#attaching function to an endpoint
@app.get('/')
def index():
    return {'message' : "Hello World !"}


#query and path parameters
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str] = None):
    return {'message' : f'blog_id-> {id}, comment_id -> {comment_id}, valid : {valid}, username:{username}'}

#optional parameters

@app.get('/blog/all')
def get_blogs(page = 1, pagesize : Optional[int] = None):
    return {'message' : f'There are {pagesize} pages on page {page}'}
#query parameters(defined values)

@app.get('/blog/all')
def get_blogs(page = 1, pagesize = 10):
    return {'message' : f'There are {pagesize} pages on page {page}'}

# predefined values
class BlogType(str,Enum) :
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type:BlogType):
    return {'message' : f'Blog type {type}'}

#path parameters
@app.get('/blog/{id}')
def index2(id):
    return { 'message' : f"blog with id {id}"}

